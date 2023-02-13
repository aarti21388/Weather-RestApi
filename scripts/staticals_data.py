from django.db import connections

def run():
        print ("I am a script for calculating statistic data")

with connections['LOANS'].cursor() as cursor:           

    cursor.execute('''INSERT INTO statistic 
    (station, weather_date, final_max_temp, final_mini_temp, final_precip) 
SELECT station, substring(weather_date,1,4), avg(maximum_temperature),avg(minimum_temperature), sum(precipitation)
from ( select * from weather where maximum_temperature<> -9999 and minimum_temperature<>-9999 and precipitation<>-9999
                )as foo 
                group by station , substring(weather_date,1,4)
                order by station''')

    connections['LOANS'].commit()
