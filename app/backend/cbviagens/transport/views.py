from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transport
from .serializers import TransportSerializer

from django.db.models import IntegerField, DecimalField
from django.db.models.functions import Cast

from .ultis import load_data

class TransportAPIView(APIView):
    def get(self, request):

        load_data()

        queryset = Transport.objects.all()
        transport_serializer = TransportSerializer(queryset, many=True)

        return Response(transport_serializer.data)

class TransportBestAlternativesAPIView(APIView):
    def get(self, request, *args, **kwargs):

        load_data()

        city = kwargs.get('city')

        queryset = Transport.objects.filter(city=city)

        min_price_econ = queryset.order_by('price_econ').first()
        min_duration_confort = queryset.order_by('duration').first()

        serializer_price = TransportSerializer(min_price_econ)
        serializer_duration = TransportSerializer(min_duration_confort)
        return Response({
            "duration": serializer_duration.data,
            "price_econ": serializer_price.data
        })
