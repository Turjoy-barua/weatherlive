import fetch
import datetime 
import matplotlib.pyplot as plt



def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def date():
    print("enter the ")
    today = datetime.date.today()
    day, month, year = (map(int, input("-->").split("/")))
    total_days = datetime.date(today.year, today.month, today.day)  - datetime.date(year, month, day)
    days_before = today - datetime.timedelta(days= 20)
    
    
    
    return (day, month, year, total_days.days, days_before)    
print(date())



def temp_trend(num_of_days):
    temp = []
    feels_like = []
    date = []
    today = datetime.datetime.now()
    day = today.day
    while day >= (today.day - num_of_days):
        data = fetch.fetch_24(today.year, today.month, day, "paris")
        date.append(day)
        temp.append(kel_to_c(data["data"][0]["temp"]))
        feels_like.append(kel_to_c(data["data"][0]["feels_like"]))
        #print(json.dumps(data, indent=2)) #--> gonna use to checks
        day-=1
    print(date)
    print(temp)
    # temp.reverse()
    # feels_like.reverse()
    
    # --> temp graph
    plt.suptitle(f"Temperature trend of last {num_of_days} days")
    plt.xlabel("date")
    plt.ylabel("Temperature")
    plt.plot(date,temp, marker="o", color = "r")
    # plt.plot(feels_like, marker='o', color = 'b')
    plt.show()   
    return(temp, feels_like)


def humidity_trend(num_of_days):
    humidity = []
    date = []
    today = datetime.datetime.now()
    day = today.day
    while day >= (today.day - num_of_days):
        data = fetch.fetch_24(today.year, today.month, day, "paris")
        date.append(day)
        humidity.append(data["data"][0]["humidity"])
        #print(json.dumps(data, indent=2)) # --> gonna use to checks
        day-=1
    # humidity.reverse()
    
    # --> humidity graph
    plt.suptitle(f"Humidity of last {num_of_days} days")
    plt.xlabel("date")
    plt.ylabel("Temperature")
    plt.plot(date, humidity, marker="o", color = "g")
    plt.show()
    return(humidity)


def rain_trend(num_of_days):
    rain = []
    date = []
    today = datetime.datetime.now()
    day = today.day
    while day >= (today.day - num_of_days):
        data = fetch.fetch_24(today.year, today.month, day, "paris")
        date.append(day)
        rain_info = (data["data"][0].get("rain", 0))
        if rain_info!=0 : 
            quantity = (list(rain_info.values())[0]) 
            rain.append(float(quantity))
        else:
            rain.append(0)
        # print(json.dumps(data, indent=2)) # --> gonna use to checks
        day-=1
    #rain.reverse()
    
    # --> rain graph
    plt.suptitle(f"Rain trend of last {num_of_days} days")
    plt.xlabel("date")
    plt.ylabel("Rain in mm")
    plt.plot(date, rain, marker="o", color = "b")
    plt.show()
    return (rain)    
    




#--------------------------------------------------------#