from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieSerializer
from watchlist_app.models import Movie


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies)
    return Response(serializer.data)


@api_view(['GET'])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)