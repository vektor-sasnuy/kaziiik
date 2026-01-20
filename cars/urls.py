from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.cars_home, name='cars_home'),
    path('detail/', views.cars_detail, name='car_detail'),
    path('create/', views.cars_create, name='car_create'),
    path('list/', views.cars_list, name='car_list'),
]