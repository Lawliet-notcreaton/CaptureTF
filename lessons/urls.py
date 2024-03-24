from django.urls import path
from lessons.views import *

urlpatterns = [
    path('', index)
]