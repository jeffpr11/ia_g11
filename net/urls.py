from django.urls import path
from .views import *

urlpatterns = [
    path('', image, name='imagen'),
    # path('img/', image, name='imagen'),
    path('vid/', video, name='video'),
]