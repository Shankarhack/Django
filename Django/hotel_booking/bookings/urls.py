from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/<int:hotel_id>/rooms/', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
]