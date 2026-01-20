from django.urls import path
from . import views

urlpatterns = [
    path('', views.mopeds_home, name='mopeds_home'),
    path('detail/', views.moped_detail, name='moped_detail'),
    path('create/', views.moped_create, name='moped_create'),
    path('list/', views.mopeds_list, name='mopeds_list'),
]



