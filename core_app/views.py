from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from .weather import Weather
from .statistic import Statistic
from .searilizer import Statistic_seralizer,Weather_seralizer


# Create your views here.
class GetWeatherData(ListAPIView):
    queryset=Weather.objects.all()
    serializer_class=Weather_seralizer

class GetStatisticsData(ListAPIView):
    queryset=Statistic.objects.all()
    serializer_class=Statistic_seralizer
    
class WeatherStationAndDatewiseView(ListAPIView):
    serializer_class = Statistic_seralizer 

    def get_station(self,*args,**kwargs):
        return Statistic.objects.filter(station=self.kwargs['station'])

    def get_queryset(self,*args,**kwargs):
        station=self.get_station()
        return station.filter(weather_date=self.kwargs['date'])
    
