from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PROPERTY_OWNER', 'Property Owner'),
        ('STUDENT', 'Student / Tenant'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STUDENT')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def is_owner(self):
        return self.role == 'PROPERTY_OWNER'

    def __str__(self):
        return f"{self.username} - {self.role}"
