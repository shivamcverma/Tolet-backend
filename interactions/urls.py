from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
]
