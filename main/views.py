from django.shortcuts import get_object_or_404, render
from .models import Hotel, Room, HotelImage, FAQ
from datetime import datetime


def home(request):
    hotels = Hotel.objects.all().order_by('-rating')  # Display hotels ordered by rating
    faqs = FAQ.objects.all()
    context = {"hotels": hotels, "faqs": faqs}

    return render(request, "home.html", context)


def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    rooms = hotel.rooms.all()  # Get all rooms for the selected hotel
    images = hotel.images.all()  # Get all images for the selected hotel
    faqs = hotel.faqs.all()  # Get all FAQs related to the hotel

    context = {"hotel": hotel, "rooms": rooms, "images": images, "faqs": faqs}
    return render(request, "hotel_detail.html", context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    hotel = room.hotel
    images = hotel.images.all()  # Display images of the hotel where the room belongs

    context = {"room": room, "hotel": hotel, "images": images}
    return render(request, "room_detail.html", context)


def about(request):
    hotels = Hotel.objects.all()
    faqs = FAQ.objects.all()

    return render(request, "about.html", {"hotels": hotels, "faqs": faqs})


def contact(request):
    hotels = Hotel.objects.all()
    faqs = FAQ.objects.all()

    return render(request, "contact.html", {"hotels": hotels, "faqs": faqs})


def search(request):
    hotels = Hotel.objects.all().order_by('-rating')  # Display hotels by rating
    faqs = FAQ.objects.all()

    # Extract query parameters from the URL
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    location = request.GET.get('location')
    guests = request.GET.get('guests')

    available_rooms = Room.objects.filter(is_available=True)

