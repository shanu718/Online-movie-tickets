from django.urls import path
from .views import book_ticket, my_bookings

urlpatterns = [
    path('<int:showtime_id>/', book_ticket, name='book_ticket'),
    path('my/', my_bookings, name='my_bookings'),
]
