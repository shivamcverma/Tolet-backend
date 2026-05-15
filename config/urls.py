from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ❌ REMOVE THIS
# from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

# ✅ IMPORT CUSTOM VIEW
from users.views import MyTokenObtainPairView


schema_view = get_schema_view(
    openapi.Info(
        title="Tolet API",
        default_version='v1',
        description="Tolet Backend APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include('properties.urls')),

    path('api/users/', include('users.urls')),

    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        )
    ),

    # ✅ CUSTOM JWT LOGIN
    path(
        'api/token/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    # ✅ REFRESH TOKEN
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

]
