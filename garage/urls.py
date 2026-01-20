from django.urls import path
from . import views

urlpatterns = [
    path('', views.garage_list, name='garage_list'),
    path('create/', views.create_garage, name='garage_create'),
    path('<int:pk>/', views.garage_detail, name='garage_detail'),
    path('<int:garage_pk>/add/', views.add_to_garage, name='add_to_garage'),
    path('<int:garage_pk>/remove/<int:item_pk>/', views.remove_from_garage, name='remove_from_garage'),
]
