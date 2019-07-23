from .models import Flight, Booking
from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializer import FlightSerializer, BookingSerializer
from datetime import date

class FlightView(ListAPIView):
		queryset = Flight.objects.all()
		serializer_class = FlightSerializer

class BookingView(ListAPIView):
		queryset = Booking.objects.filter(date__gt=  date.today())
		serializer_class = BookingSerializer