from rest_framework import serializers
from .models import Favorite, Report
from properties.serializers import PropertySerializer

class FavoriteSerializer(serializers.ModelSerializer):
    property_details = PropertySerializer(source='property', read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'property', 'property_details', 'created_at')
        read_only_fields = ('user',)

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'user', 'property', 'reason', 'created_at', 'is_resolved')
        read_only_fields = ('user', 'is_resolved')
