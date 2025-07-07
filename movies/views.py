from django.shortcuts import render
from .models import Movie, Showtime

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def showtimes(request, movie_id):
    showtimes = Showtime.objects.filter(movie_id=movie_id)
    return render(request, 'movies/showtimes.html', {'showtimes': showtimes})




