from django.shortcuts import render, redirect
from .forms import RoomForm, GuestForm
from .models import Room
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # redirect to room list page
    else:
        form = RoomForm()
    return render(request, 'rooms/add_room.html', {'form': form})

def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # or guest list page
    else:
        form = GuestForm()
    return render(request, 'rooms/add_guest.html', {'form': form})
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})