from django.db import models
from django.conf import settings

class Property(models.Model):
    PROPERTY_TYPES = (
        ('ROOM', 'Room'),
        ('PG', 'Paying Guest (PG)'),
        ('FLAT', 'Flat'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Location
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    amenities = models.JSONField(default=dict, blank=True) # e.g. {"wifi": True, "ac": False}
    
    is_available = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"
