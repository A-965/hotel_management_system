from django.db import models

class Room(models.Model):
    ROOM_STATUS = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    )
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ROOM_STATUS, default='available')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Room {self.number} ({self.get_status_display()})"

class Guest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='guests')
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
