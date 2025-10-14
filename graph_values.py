import fetch
import datetime 
import json
import pandas as pd

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def date(): # ---> used to solve the problem with days counting
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days= int(20))
    return (start_date, end_date)    




def trend(city):
    temp = []
    feels_like = []
    date_list = []
    humidity = []
    rain = []
    try :
        start_date, end_date = date()
    except:
        return("missing input")
    while start_date <= end_date:
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, city)
        date_list.append(start_date.strftime('%d/%b'))
        temp.append(kel_to_c(data["data"][0]["temp"]))
        feels_like.append(kel_to_c(data["data"][0]["feels_like"]))
        humidity.append(data["data"][0]["humidity"])
        rain_info = (data["data"][0].get("rain", 0))
        if rain_info!=0 : 
            quantity = (list(rain_info.values())[0]) 
            rain.append(float(quantity))
            
        else:
            rain.append(0)
        
        #print(temp)
        #print(json.dumps(data, indent=2)) #--> gonna use to checks
        start_date += datetime.timedelta(days=1)
    d = {'dates': date_list, 'temp': temp, 'feels_like': feels_like, 'humidity': humidity, 'rain': rain}
    data_frame = pd.DataFrame(data=d)
    print(data_frame)
    return(data_frame)

