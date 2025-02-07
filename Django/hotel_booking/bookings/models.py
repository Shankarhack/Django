from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    total_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()

    def save(self, *args, **kwargs):
        if self.room.is_available:
            self.room.is_available = False
            self.room.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Room is already booked!")

    def cancel_booking(self):
        self.room.is_available = True
        self.room.save()
        self.delete()

    def __str__(self):
        return f"{self.customer_name} - {self.room}"
