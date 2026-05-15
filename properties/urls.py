from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet
from rest_framework.routers import DefaultRouter

from .views import (
    PropertyViewSet,
    RoomViewSet
)


router = DefaultRouter()

router.register('properties', PropertyViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = router.urls


