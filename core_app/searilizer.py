from rest_framework import serializers
from .weather import Weather
from .statistic import Statistic

class Weather_seralizer(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields=['id','station','weather_date','maximum_temperature','minimum_temperature','precipitation']

class Statistic_seralizer(serializers.ModelSerializer):
    class Meta:
        model=Statistic
        fields=['id','station','weather_date','final_max_temp','final_mini_temp','final_precip']