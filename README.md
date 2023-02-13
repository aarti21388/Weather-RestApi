
# Weather Data API

This project shows how to build a basic data access application that continuously runs in the background, processing a variety of weather data from different station including weather date,maximum temperature,minimum temperature and precipitation 

## 
## Getting Started 

1. Install all library use Pip install -r requirements.txt

2. Clone this repository

   ```
   git clone git@github.com:aarti21388/Weather-RestApi.git
   cd Weather_ReatApi
   ```

3. Run python script to read Wx_data folder for weater data file use 

   ```
   python manage.py runscript import_weather
   ```

4. Run python script to calculating statistics.

   ```
   python manage.py runscript staticals_data
   ```

5  Use these endpoints to return a JSON-formatted response with a representation of the ingested/calculated
'''
http://127.0.0.1:8000/ [swagger view]
http://127.0.0.1:8000/api/weather/ [weather data paginated]
http://127.0.0.1:8000/api/weather/stats/ [statistics data paginated]
http://127.0.0.1:8000/api/weather/stats/USC00110187/1994/ [filter the response by year and station ID]
'''
