
# Weather Data API using Django REST framework

This project shows how to build a basic data access application using Django REST framework with generic views and process a variety of weather data from different station including weather date,maximum temperature,minimum temperature and precipitation. Use postgres database for creating a database schema. And docker-compose.yaml file to run container for postgres.Require postgres instance to connect database to create schema

## 
## Getting Started 

1. Install all library use
   ```
   Pip install -r requirements.txt
   ```
2. Clone this repository

   ```
   git clone git@github.com:aarti21388/Weather-RestApi.git
   cd Weather_ReatApi
   ```
## 
##  use inspectdb. Introspects the database tables in the database pointed-to by the DATABASE_NAME setting and outputs a Django model module (a models.py file) to standard output
   ```
   python manage.py inspectdb --database LOANS weather > core_app/weather.py
   ```
   ```
   python manage.py inspectdb --database LOANS statistic > core_app/statics.py
   ```
## 
## Run python script to read Wx_data folder for weater data file use 

   ```
   python manage.py runscript -v 2 import_weather
   ```

   Run python script to calculating statistics.

   ```
  python manage.py runscript -v 2 staticals_data
   ```

## 
##  Use these endpoints to return a JSON-formatted response with a representation of the ingested/calculated
   
   ```
   http://127.0.0.1:8000/ [swagger view]
   ```
   ```
   http://127.0.0.1:8000/api/weather/ [weather data paginated])
   ```
   ```
    http://127.0.0.1:8000/api/weather/stats/ [statistics data paginated]
   ```
   ```
   http://127.0.0.1:8000/api/weather/stats/USC00110187/1994/ [filter the response by year and station ID]
   ```
      
## 
## To run test
   ```
   python manage.py test core_app
   ```
## 
## To Deploy your First Rest API with AWS we can use Amazon ECS.
   ```
   1. 1) Launching an EC2 instance
      2) Connecting the EC2 instance on local machine
      3) Configure EC2 instance (Install Apache2, pip, apache module for wsgi, and virtual environment)
      4) Clone the Django Application Repository.
      5) Create a virtual Environment
      6) Install the necessary packages
      7)Test run the application
      8) Configure Apache to point to our django application
   ```
   ```
   2. To access data from your backend servies we can use Lambda or EC2
   ```
   ```
   3.Amazon RDS for the database. Amazon RDS supports 6 familiar engines, including 3 open source databases: MySQL, PostgreSQL, and MariaDB.
   ```
   ```
   4.To schedule version of your data ingestion code we can use AWS Glue
   ```
   ```
   5. We can use cloud watch event rule to trigger the lambda function using cron job to run everyday 
      (a) lambda function gets the report of all ec2 instances in the account.
      (b) uploads the report to the s3 bucket 
   ```
   
