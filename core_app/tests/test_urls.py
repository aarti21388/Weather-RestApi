
# to run test run python manage.py test core_app
from django.test import SimpleTestCase
from django.urls import reverse,resolve


from core_app.views import GetStatisticsData,GetWeatherData

class ApiUrlTests(SimpleTestCase):

    #test for  #http://127.0.0.1:8000/api/weather/ (to get all weather data)
    def test_get_weather_is_resolved(self):

        url=reverse('weather')#to get absolute path
        #print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class,GetWeatherData) 
    
    def test_get_statics_is_resolved(self):
        url=reverse('statistic')
        #print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,GetStatisticsData)

