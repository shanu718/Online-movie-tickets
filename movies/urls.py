from django.urls import path
from .views import movie_list, showtimes

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('showtimes/<int:movie_id>/', showtimes, name='showtimes'),

]
