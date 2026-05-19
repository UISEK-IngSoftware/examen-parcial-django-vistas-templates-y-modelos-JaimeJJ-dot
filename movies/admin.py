from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director_name', 'publication_year', 'image')
    search_fields = ('title', 'director_name', 'genre')
