"""django_shreeram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home, search, about, contact, hotel_detail, room_detail
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),  # Home page to display hotels and FAQs
    path('search/', search, name="search"),  # Search for hotels and rooms
    path('about/', about, name="about"),  # About page
    path('contact/', contact, name="contact"),  # Contact page
    path('hotel/<slug:slug>/', hotel_detail, name="hotel_detail"),  # Hotel detail page with rooms and images
    path('room/<slug:slug>/', room_detail, name="room_detail"),  # Room detail page
    path('search_result/', views.search_result, name='search_result'),  # Add this line

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Hotel Admin"
admin.site.site_title = "Hotel Admin Portal"
admin.site.index_title = "Welcome to the Hotel Admin Portal"
