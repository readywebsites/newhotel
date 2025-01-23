from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    facilities = models.TextField(help_text="List of facilities, e.g., Wi-Fi, Pool, Gym")
    image = models.ImageField(upload_to='hotel_images/')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hotel_detail', kwargs={'slug': self.slug})


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=100, help_text="e.g., Single, Double, Suite")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(help_text="Number of people the room can accommodate")
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.hotel.name}-{self.room_type}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'slug': self.slug})


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f"Image for {self.hotel.name}"


class FAQ(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, default=1)  # Use string reference for Hotel model
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ: {self.question} ({self.hotel.name})"
