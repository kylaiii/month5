from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import *


# Create your views here.
class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieItemUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorItemUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewItemUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
# @api_view(['GET', 'POST'])
# def director_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data)
#     if request.method == 'POST':
#         name = request.data.get('name', '')
#         director = Director.objects.create(name=name)
#         director.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={
#                             "message": "created successfully",
#                             "director": DirectorSerializer(director).data
#                         })
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_view(request, **kwargs):
#     try:
#         director = Director.objects.get(id=kwargs['id'])
#     except Director.DoesNotExist:
#         return Response(data={"error": "Director with that id does not exists"})
#     if request.method == 'GET':
#         data = DirectorSerializer(director, many=False).data
#         return Response(data=data)
#     if request.method == 'PUT':
#         name = request.data.get('name', '')
#         director.name = name
#         director.save()
#         return Response(
#             data={"message": "director created successfully", "director": DirectorSerializer(director).data})
#     if request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def movie_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#
#     if request.method == 'POST':
#         title = request.data.get("title", "")
#         description = request.data.get("description", "")
#         duration = request.data.get("duration", 0)
#         director_id = request.data.get("director_id", 1)
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         movie.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={"message": "movie created successfully", "movie": MovieSerializer(movie).data})
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_view(request, **kwargs):
#     try:
#         movie = Movie.objects.get(id=kwargs['id'])
#     except Movie.DoesNotExist:
#         return Response(data={"error": "movie does not exists"})
#     if request.method == "GET":
#         data = MovieSerializer(movie, many=False).data
#         return Response(data=data)
#
#     if request.method == 'PUT':
#         title = request.data.get("title", movie.title)
#         description = request.data.get("description", movie.description)
#         duration = request.data.get("duration", movie.duration)
#         director_id = request.data.get("director_id", movie.director_id)
#         movie.title = title
#         movie.description = description
#         movie.duration = duration
#         movie.director_id = director_id
#         movie.save()
#
#         return Response(data={"message": "movie updated successfully", "movie": MovieSerializer(movie).data})
#
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(data={"message": "movie deleted successfully"})
#
#
# @api_view(['GET', 'POST'])
# def review_view(request):
#     reviews = Review.objects.all()
#     serializer = ReviewSerializer(reviews, many=True)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_view(request, **kwargs):
#     try:
#         review = Review.objects.get(id=kwargs['id'])
#     except Review.DoesNotExist:
#         return Response(data={"error", "review does not exists"})
#
#     if request.method == 'GET':
#         data = ReviewSerializer(review, many=False).data
#         return Response(data=data)
#
#     if request.method == 'DELETE':
#         review.delete()
#         return Response(data={"message": "review deleted successfully"})
#
#     if request.method == 'PUT':
#         author_id = request.data.get("author_id", review.author_id)
#         text = request.data.get("text", review.text)
#         stars = request.data.get("stars", review.stars)
#         movie_id = request.data.get("movie_id", review.movie_id)
#
#         review.author_id = author_id
#         review.text = text
#         review.stars = stars
#         review.movie_id = movie_id
#
#
@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)