from django.contrib import admin
from .models import Movie,UserMovieList

# Register your models here.
admin.site.register(Movie)

admin.site.register(UserMovieList)