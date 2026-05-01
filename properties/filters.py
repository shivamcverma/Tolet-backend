import math
import django_filters
from .models import Property

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

class PropertyFilter(django_filters.FilterSet):
    min_rent = django_filters.NumberFilter(field_name="rent", lookup_expr='gte')
    max_rent = django_filters.NumberFilter(field_name="rent", lookup_expr='lte')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    
    # Distance based custom filtering
    latitude = django_filters.NumberFilter(method='filter_by_distance')
    longitude = django_filters.NumberFilter(method='filter_by_distance')
    radius = django_filters.NumberFilter(method='filter_by_distance')

    class Meta:
        model = Property
        fields = ['property_type', 'city', 'is_verified']

    def filter_by_distance(self, queryset, name, value):
        # We only want to execute distance filter once if lat, lon, and radius are provided in request
        lat = self.data.get('latitude')
        lon = self.data.get('longitude')
        rad = self.data.get('radius', 5) # default 5km

        if not (lat and lon):
            return queryset

        try:
            lat = float(lat)
            lon = float(lon)
            rad = float(rad)
        except ValueError:
            return queryset

        # Calculate distances and filter
        # Since this is a simple python loop, it's not scalable for millions of records,
        # but suitable for basic implementation. For production, PostGIS is recommended.
        
        filtered_ids = []
        for prop in queryset:
            if prop.latitude and prop.longitude:
                dist = haversine_distance(lat, lon, prop.latitude, prop.longitude)
                if dist <= rad:
                    filtered_ids.append(prop.id)
                    
        return queryset.filter(id__in=filtered_ids)
