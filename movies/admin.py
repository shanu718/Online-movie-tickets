from django.contrib import admin
from .models import Movie, Theater, Showtime

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Showtime)

