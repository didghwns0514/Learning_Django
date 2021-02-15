from django.urls import path

# create my view links here
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]