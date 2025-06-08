from django.shortcuts import render, redirect
from .models import Booking
from guests.models import Guest
from rooms.models import Room

def booking_form(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']

        guest, created = Guest.objects.get_or_create(
            email=email,
            defaults={'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number}
        )

        booking = Booking.objects.create(
            guest=guest,
            room=room,
            check_in=check_in,
            check_out=check_out
        )

        room.is_available = False
        room.save()

        return redirect('room_list')

    return render(request, 'bookings/booking_form.html', {'room': room})
