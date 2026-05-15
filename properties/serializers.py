from rest_framework import serializers
from .models import Property, Room

from rest_framework import serializers

from .models import Property, Room


class PropertySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(
        source='owner.email'
    )

    class Meta:
        model = Property

        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room

        fields = '__all__'