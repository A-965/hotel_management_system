from django import forms
from .models import Room, Guest

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'room_type', 'status', 'price']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['full_name', 'email', 'phone', 'room', 'check_in', 'check_out']
