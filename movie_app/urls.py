from django.urls import path
from .views import *

urlpatterns = [
    path('directors/', DirectorListAPIView.as_view()),
    path('directors/<int:pk>/', DirectorItemUpdateDestroyAPIView.as_view()),
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<int:pk>/', MovieItemUpdateDestroyAPIView.as_view()),
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewItemUpdateDestroyView.as_view()),
    path('movies/reviews/', movies_reviews_view)
]