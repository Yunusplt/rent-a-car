from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ReservationViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)                  # 'Car' modeli için viewset
router.register('reservations', ReservationViewSet)  # 'Reservation' modeli için viewset


urlpatterns = [
    path('', include(router.urls)),
]