from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *

urlpatterns = [
    path('movies/', movie_view),
    path('movies/<int:id>/', movie_detail_view),
    path('directors/', director_view),
    path('directors/<int:id>/', director_detail_view),
    path('reviews/', review_view),
    path('reviews/<int:id>/', review_detail_view),
    path('movies/reviews/', movies_reviews_view)
]