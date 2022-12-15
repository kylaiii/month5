from rest_framework.decorators import api_view, action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from .models import *
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        director = Director.objects.create(
            name=name
        )
        director.save()
        return Response(status=status.HTTP_201_CREATED, data={ "message": "director created successfully",
                                                               "director": DirectorSerializer(director).data })


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(data={ "error": "Director with that id does not exists" })
    if request.method == 'GET':
        data = DirectorSerializer(director, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        director.name = name
        director.save()
        return Response(
            data={ "message": "director updated successfully", "director": DirectorSerializer(director).data })
    if request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_view(request: Request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        duration = serializer.validated_data['duration']
        director_id = serializer.validated_data['director_id']
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={ "message": "movie created successfully", "movie": MovieSerializer(movie).data })


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request: Request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(data={ "error": "movie does not exists" })
    if request.method == "GET":
        data = MovieSerializer(movie, many=False).data
        return Response(data=data)

    if request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        duration = serializer.validated_data['duration']
        director_id = serializer.validated_data['director_id']
        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        movie.save()

        return Response(data={ "message": "movie updated successfully", "movie": MovieSerializer(movie).data })

    if request.method == 'DELETE':
        movie.delete()
        return Response(data={ "message": "movie deleted successfully" })


@api_view(['GET', 'POST'])
def review_view(request: Request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        author_id = serializer.validated_data['author_id']
        text = serializer.validated_data['text']
        stars = serializer.validated_data['stars']
        movie_id = serializer.validated_data['movie_id']

        review = Review.objects.create(
            author_id=author_id,
            text=text,
            stars=stars,
            movie_id=movie_id
        )
        review.save()
        return Response(data={ "message": "review created successfully", "review": ReviewSerializer(review).data })


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(data={ "error": "review does not exists" })

    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data)

    if request.method == 'DELETE':
        review.delete()
        return Response(data={ "message": "review deleted successfully" })

    if request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author_id = serializer.validated_data['author_id']
        text = serializer.validated_data['text']
        stars = serializer.validated_data['stars']
        movie_id = serializer.validated_data['movie_id']

        review.author_id = author_id
        review.text = text
        review.stars = stars
        review.movie_id = movie_id

        review.save()

        return Response(data={ "message": "review updated successfully", "review": ReviewSerializer(review).data })


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)