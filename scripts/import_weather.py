import os,time,shutil
from core_app.weather import Weather


start_time = time.time()
print("Weather data reading...")
path=f"{os.getcwd()}/wx_data"

def read_text_file(files):
    for f in files:
        file_path=f"{path}/{f}"
        with open(file_path,"r") as data_read:
            lines=[l.rstrip() for l in data_read]
            for line in lines:
                data=line.split('\t')
                w=Weather.objects.create(station=f[:-4],weather_date=int(data[0]),maximum_temperature=int(data[1]),minimum_temperature=int(data[2]),precipitation=int(data[3]))
                w.save()
        
        shutil.move(file_path,f"{os.getcwd()}/process_wx_data/{f}")
    
read_text_file(os.listdir(path))

end_time = time.time()

total_time = end_time - start_time

print("Start time: ", start_time)
print("End time: ", end_time)
print("Total time: ", total_time)

