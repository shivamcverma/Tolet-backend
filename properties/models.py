from django.db import models
from users.models import User


class Property(models.Model):
    PROPERTY_TYPES = (
        ('hostel', 'Hostel'),
        ('pg', 'PG'),
        ('room', 'Room'),
        ('flat', 'Flat'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        null=True,
        blank=True
    )
    city = models.CharField(max_length=100)
    address = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Room(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    room_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    capacity = models.IntegerField()
    rent = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    def __str__(self):
        return f"{self.property.title} - Room {self.room_number}"