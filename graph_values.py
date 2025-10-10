import fetch
import datetime 
import matplotlib.pyplot as plt
import json
import pandas as pd
def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def date():
    end_date = datetime.date.today()
    user_input = "20" #input('''How many past days would you like to analyze? 
#(Example: 7 for last week, 30 for last month, 60 for last two months or date to choose any past days from today)\n''')
    if user_input.isdigit():
        start_date = end_date - datetime.timedelta(days= int(user_input))
    elif user_input == "custom":
        print("enter date: day/month/year\n ")
        day, month, year = (map(int, input("-->").split("/")))
        start_date = datetime.date(year, month, day)
    else:
        #print(type(user_input))
        return("missing input")
    total_days = (start_date - end_date).days + 1    
    return (start_date, end_date, total_days)    


""" How many past days would you like to analyze? 
(Example: 7 for last week, 30 for last month, 60 for last two months) """

def trend(city):
    temp = []
    feels_like = []
    date_list = []
    humidity = []
    rain = []
    try :
        start_date, end_date, total_days = date()
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

""" 
def humidity_trend():
    city = "paris"#input("Enter your city : ")
    humidity = []
    dates_list = []
    
    try :
        start_date, end_date, total_days = date()
    except:
        return("missing input")
    while start_date <= (end_date):
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, city)
        dates_list.append(start_date.strftime('%d/%b'))
        humidity.append(data["data"][0]["humidity"])
        #print(json.dumps(data, indent=2)) # --> gonna use to checks
        #print(humidity)
        start_date += datetime.timedelta(days=1)
    # humidity.reverse()
    # --> humidity graph
    plt.suptitle(f"Humidity of last {total_days} days")
    plt.xlabel("date")
    plt.ylabel("humidity %")
    plt.plot(dates_list, humidity, marker="o", color = "g")
    plt.xticks(rotation = 70)
    plt.show() 
    return(humidity)


def rain_trend():
    city = input("Enter your city : ")
    rain = []
    date_list = []
    try:
        start_date, end_date, total_days = date()
    except:
        return("missing input")
    while start_date <= end_date:
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, city)
        date_list.append(start_date.strftime('%d/%b'))
        rain_info = (data["data"][0].get("rain", 0))
        if rain_info!=0 : 
            quantity = (list(rain_info.values())[0]) 
            rain.append(float(quantity))
            
        else:
            rain.append(0)
        #print(json.dumps(data, indent=2)) # --> gonna use to checks
        #print(rain)
        start_date += datetime.timedelta(days=1)
    #rain.reverse()
    
    # --> rain graph
    plt.suptitle(f"Rain trend of last {total_days} days")
    plt.xlabel("date")
    plt.ylabel("Rain in mm")
    plt.plot(date_list, rain, marker="o", color = "b")
    plt.xticks(rotation = 70)
    plt.show()
    return (rain)     """
    


#--------------------------------------------------------#