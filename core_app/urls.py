from django.urls import path
from . import views

urlpatterns=[
    
    path("weather/",views.GetWeatherData.as_view(),name="weather"),
    path("weather/stats/",views.GetStatisticsData.as_view(),name='statistic'),
    path("weather/stats/<str:station>/<str:date>/",views.WeatherStationAndDatewiseView.as_view(),name='weather_station_date'),
   
]

#http://127.0.0.1:8000/api/weather/ (to get all weather data)
#http://127.0.0.1:8000/api/weather/stats/ ( to get all calculated data)
#http://127.0.0.1:8000/api/weather/stats/USC00110338/2001/ (to filter the response by date and station ID)