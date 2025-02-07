from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hotel, Room, Booking
from .forms import BookingForm
from django.db.models import Q

def hotel_list(request):
    query = request.GET.get('q', '')
    hotels = Hotel.objects.all()

    if query:
        hotels = hotels.filter(Q(name__icontains=query) | Q(location__icontains=query))

    return render(request, 'bookings/hotel_list.html', {'hotels': hotels, 'query': query})

def room_list(request, hotel_id):
    """List all rooms of a hotel, with filtering by availability."""
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = hotel.room_set.all()

    # Check if the user is filtering by availability
    available_filter = request.GET.get('available')
    if available_filter == 'true':
        rooms = rooms.filter(is_available=True)

    return render(request, 'bookings/room_list.html', {'hotel': hotel, 'rooms': rooms})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if not room.is_available:
        messages.error(request, "This room is already booked.")
        return redirect('hotel_list')

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.hotel = room.hotel
            booking.save()
            messages.success(request, "Room booked successfully!")
            return redirect('booking_confirmation', booking_id=booking.id)
        else:
            messages.error(request, "There was an error with your booking.")
    else:
        form = BookingForm(initial={'room': room, 'hotel': room.hotel})

    return render(request, 'bookings/book_room.html', {'form': form, 'room': room})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.cancel_booking()
    messages.success(request, "Booking cancelled successfully!")
    return redirect('hotel_list')
