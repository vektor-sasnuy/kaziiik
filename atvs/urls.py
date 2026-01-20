from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.atvs_home, name='atvs_home'),
    path('detail/', views.atvs_detail, name='atv_detail'),
    path('create/', views.atvs_create, name='atv_create'),
    path('list/', views.mopeds_list, name='atv_list'),
]
