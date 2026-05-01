from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'city', 'property_type', 'rent', 'is_available', 'is_verified')
    list_filter = ('property_type', 'is_available', 'is_verified', 'city')
    search_fields = ('title', 'city', 'area')
    inlines = [PropertyImageInline]
    
    actions = ['mark_verified', 'mark_unverified']

    def mark_verified(self, request, queryset):
        queryset.update(is_verified=True)
    mark_verified.short_description = "Mark selected properties as verified"

    def mark_unverified(self, request, queryset):
        queryset.update(is_verified=False)
    mark_unverified.short_description = "Mark selected properties as unverified"

admin.site.register(Property, PropertyAdmin)
