from django.urls import path
from . import views
from .views import new,home,aboutus,resultsPage

urlpatterns = [
    path('', views.home, name='home'),
    path('home/',new),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('results/', views.resultsPage, name='results'),
    

]