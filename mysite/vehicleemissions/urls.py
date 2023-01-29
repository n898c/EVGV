from django.urls import path
from . import views
from .views import new

urlpatterns = [
    path('', views.home, name='home'),
    path('home/',new),
]