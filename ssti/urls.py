from django.urls import path
from . import views

urlpatterns = [
    path('practice', views.index, name='index'),
    path('', views.start),
]