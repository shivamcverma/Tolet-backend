from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .models import Property, Room
from .serializers import (
    PropertySerializer,
    RoomSerializer
)


class PropertyViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all()

    serializer_class = PropertySerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(
            owner=self.request.user
        )


class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()

    serializer_class = RoomSerializer

    permission_classes = [IsAuthenticated]