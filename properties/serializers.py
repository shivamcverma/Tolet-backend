from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ('id', 'image', 'uploaded_at')

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    owner_username = serializers.ReadOnlyField(source='owner.username')
    owner_phone = serializers.ReadOnlyField(source='owner.phone_number')

    class Meta:
        model = Property
        fields = (
            'id', 'owner', 'owner_username', 'owner_phone', 'title', 'description', 
            'rent', 'city', 'area', 'latitude', 'longitude', 'property_type', 
            'amenities', 'is_available', 'is_verified', 'created_at', 'updated_at',
            'images', 'uploaded_images'
        )
        read_only_fields = ('owner', 'is_verified', 'created_at', 'updated_at')

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        property_obj = Property.objects.create(**validated_data)
        
        for image in uploaded_images:
            PropertyImage.objects.create(property=property_obj, image=image)
            
        return property_obj
