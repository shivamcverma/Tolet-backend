from django.shortcuts import render

# 🔥 DRF
from rest_framework import generics

# 🔥 MODELS & SERIALIZERS
from .models import User
from .serializers import UserRegisterSerializer

# 🔥 JWT
from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt import MyTokenObtainPairSerializer


# ✅ REGISTER VIEW
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = UserRegisterSerializer


# ✅ CUSTOM JWT LOGIN VIEW
class MyTokenObtainPairView(
    TokenObtainPairView
):

    serializer_class = MyTokenObtainPairSerializer