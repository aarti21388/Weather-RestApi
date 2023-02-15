from django.db import connections
import logging,time

logging.basicConfig(filename='log/ingestion.log',
                  level=logging.INFO, 
     format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S')
logger = logging.getLogger("statistics")

start_time = time.time()
logger.info(f"calculating these statistics of data.......{start_time}")

def run():
        print ("I am a script for calculating statistic data")


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
end_time = time.time()

total_time = (end_time - start_time)


logger.info(f"End time: {end_time}")
logger.info(f"calculate statistic data {total_time} ")


