from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from datetime import datetime,date

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(availability=True)
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        
        if self.request.user.is_staff: 
            return queryset
        else:
            queryset = Car.objects.filter(date_departure__gt=now)           
            return queryset

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


