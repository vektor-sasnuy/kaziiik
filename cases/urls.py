from django.urls import path
from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('<int:pk>/', views.case_detail, name='case_detail'),
    path('<int:pk>/open/', views.open_case, name='open_case'),
    path('<int:pk>/open-animation/', views.open_case_animation, name='open_case_animation'),
    path('history/', views.cases_history, name='history'),
]
