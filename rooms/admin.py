from django.contrib import admin
from .models import Room, Guest

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'room_type', 'status', 'price']
    list_filter = ['status', 'room_type']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'room', 'check_in', 'check_out']
    list_filter = ['check_in', 'check_out']
