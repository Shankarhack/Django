from django.contrib import admin
from .models import Hotel, Room, Booking

class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'total_rooms')
    search_fields = ('name', 'location')
    inlines = [RoomInline]

class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_number', 'is_available')
    list_filter = ('hotel', 'is_available')
    search_fields = ('room_number',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'hotel', 'room', 'check_in', 'check_out')
    list_filter = ('hotel', 'check_in', 'check_out')
    search_fields = ('customer_name',)

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
