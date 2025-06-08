from django.contrib import admin
from django.urls import path ,include
from rooms.views import room_list
from bookings.views import booking_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', room_list, name='room_list'),
    path('book-room/<int:room_id>/', booking_form, name='booking_form'),
    path('', include('rooms.urls')),
]
