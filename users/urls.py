from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view),
    path('authorize/', authorize_view)
]