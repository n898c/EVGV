from django.urls import path
from . import views
from .views import new,home,aboutus,resultsPage, cars

urlpatterns = [
    path('', new, name='home'),
    path('',new),
    path('cars/', views.cars, name='cars'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('results/', views.resultsPage, name='results'),
    path('carpage',views.carpage,name='carpage'),
    

]