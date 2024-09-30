from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctors, name='dc'),
    path('doctors/<int:pk>/', views.doctor, name='o_dc'),
    path('doctors/sort/<str:name>/', views.sorted_doctors, name='s_dc'),
    path('directions/', views.directions, name='drc'),
    path('', views.home, name='main')
]
