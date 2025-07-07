from django.shortcuts import render, redirect
from .models import Booking
from movies.models import Showtime
from django.contrib.auth.decorators import login_required

@login_required
def book_ticket(request, showtime_id):
    showtime = Showtime.objects.get(id=showtime_id)
    if request.method == 'POST':
        seats = int(request.POST['seats'])
        if showtime.available_seats >= seats:
            showtime.available_seats -= seats
            showtime.save()
            Booking.objects.create(user=request.user, showtime=showtime, seats=seats)
            return redirect('my_bookings')
        else:
            return render(request, 'bookings/book_ticket.html', {
                'showtime': showtime,
                'error': 'Not enough seats available'
            })

    return render(request, 'bookings/book_ticket.html', {'showtime': showtime})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


