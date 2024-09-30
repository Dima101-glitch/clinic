from django.urls import path
from .views import DirectionListView, DoctorListView, DoctorDetailView

urlpatterns = [
    path('directions/', DirectionListView.as_view(), name='direction-list'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
