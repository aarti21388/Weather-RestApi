import os,time,shutil
from core_app.weather import Weather
import logging,time

from datetime import datetime
logging.basicConfig(filename='log/ingestion.log',
                    level=logging.INFO, 
     format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S')
logger = logging.getLogger("ingestion")
start_time = time.time()

logger.info("Weather data reading... "+str(start_time))
file_count=0
path=f"{os.getcwd()}/wx_data"
count=0


def read_text_file(files):
    count=0
    for f in files:
        file_path=f"{path}/{f}"
        logger.info(file_path) # file name will store in file_path variable
        with open(file_path,"r") as data_read:
            lines=[l.rstrip() for l in data_read] # all lines from .txt file store in lines variable
            for line in lines:
                data=line.split('\t') # data is separted by \t which will split it and store in data list
                w=Weather.objects.create(station=f[:-4],weather_date=int(data[0]),maximum_temperature=int(data[1]),minimum_temperature=int(data[2]),precipitation=int(data[3]))
                w.save() # saving to the weather model with station Id, date,tempreture and precipitation
        count+=1
        shutil.move(file_path,f"{os.getcwd()}/process_wx_data/{f}") #move process file to different folder

    return count

def main():
    c=read_text_file(os.listdir(path))

    end_time =time.time()
    total_time = end_time-start_time

    logger.info(f" end time in {end_time}")
    logger.info(f" Total time {total_time} and file count is {c}")

def run():
    print("i am a script for reading weather_data")

main()