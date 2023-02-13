# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.CharField(max_length=200, blank=True, null=True)
    weather_date = models.CharField(max_length=20)
    maximum_temperature = models.IntegerField(blank=True, null=True)
    minimum_temperature = models.IntegerField(blank=True, null=True)
    precipitation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather'

    def __str__(self):
        return f"{self.station} maximum weather on {self.weather_date} is {self.maximum_temperature} and minimum weather is {self.minimum_temperature}"