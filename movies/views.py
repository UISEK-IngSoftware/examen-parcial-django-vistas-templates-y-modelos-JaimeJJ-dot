from django.shortcuts import get_object_or_404, render

from .models import Movie


def index(request):
    movies = Movie.objects.order_by('title')
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})
