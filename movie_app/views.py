from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DrSerializer, MovieSerializer,ReviewSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DrSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:

        post = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': "Director not found"},
                        status=status.HTTP_404_NOT_FOUND)
    data = DrSerializer(post).data
    return Response(data=data)





@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        post = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': "Movie not found"},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(post).data
    return Response(data=data)



@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_view(request, id):
    try:

        post = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review not found"},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(post).data
    return Response(data=data)


