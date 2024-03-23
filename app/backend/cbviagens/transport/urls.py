from django.urls import path
from .views import TransportAPIView, TransportBestAlternativesAPIView

urlpatterns = [
    path('api/', TransportAPIView.as_view(), name='all_transport'),
    path('api/<str:city>', TransportBestAlternativesAPIView.as_view(), name='transport_filter')
    
]