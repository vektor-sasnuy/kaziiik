from django.urls import path
from . import views

urlpatterns = [
    path('', views.motocycles_home, name='motocycles_home'),
    path('detail/', views.motocycles_detail, name='motocycles_detail'),
    path('create/', views.motocycles_create, name='motocycles_create'),
    path('list/', views.motocycles_list, name='motocycles_list'),
]
