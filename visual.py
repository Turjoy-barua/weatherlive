import fetch
import datetime 
import matplotlib.pyplot as plt
import historical
import json

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def date():
    print("enter date: day/month/year\n ")
    today = datetime.date.today()
    day, month, year = (map(int, input("-->").split("/")))
    start_date = datetime.date(year, month, day)
    total_days = datetime.date(today.year, today.month, today.day)  - datetime.date(year, month, day)
    days_before = today - datetime.timedelta(days= 20)
    end_date = datetime.date.today()
    return (start_date, end_date, total_days)    


def temp_trend():
    
    temp = []
    feels_like = []
    date_list = []
    
    start_date, end_date, total_days = date()
    while start_date <= end_date:
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, "paris")
        date_list.append(start_date.strftime('%d/%m'))
        temp.append(kel_to_c(data["data"][0]["temp"]))
        feels_like.append(kel_to_c(data["data"][0]["feels_like"]))
        print(temp)
        #print(json.dumps(data, indent=2)) #--> gonna use to checks
        start_date += datetime.timedelta(days=1)
    
    # temp.reverse()
    # feels_like.reverse()
    
    # --> temp graph
    plt.suptitle(f"Temperature trend of last {total_days} days")
    plt.xlabel("date")
    plt.ylabel("Temperature")
    plt.plot(date_list,temp, marker="o", color = "r")
    # plt.plot(feels_like, marker='o', color = 'b')
    plt.show()   
    return(temp, feels_like)


def humidity_trend():
    humidity = []
    dates_list = []
    
    start_date, end_date, total_days = date()
    while start_date <= (end_date):
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, "paris")
        dates_list.append(start_date.strftime('%d/%m'))
        humidity.append(data["data"][0]["humidity"])
        print(json.dumps(data, indent=2)) # --> gonna use to checks
        start_date += datetime.timedelta(days=1)
    # humidity.reverse()

    # --> humidity graph
    plt.suptitle(f"Humidity of last {total_days} days")
    plt.xlabel("date")
    plt.ylabel("Temperature")
    plt.plot(dates_list, humidity, marker="o", color = "g")
    plt.show()
    return(humidity)


def rain_trend():
    rain = []
    date_list = []
    start_date, end_date, total_days = date()
    while start_date <= end_date:
        data = fetch.fetch_24(start_date.year, start_date.month, start_date.day, "paris")
        date_list.append(start_date.strftime('%d/%m'))
        rain_info = (data["data"][0].get("rain", 0))
        if rain_info!=0 : 
            quantity = (list(rain_info.values())[0]) 
            rain.append(float(quantity))
            
        else:
            rain.append(0)
        #print(json.dumps(data, indent=2)) # --> gonna use to checks
        print(rain)
        start_date += datetime.timedelta(days=1)
    #rain.reverse()
    
    # --> rain graph
    plt.suptitle(f"Rain trend of last {total_days} days")
    plt.xlabel("date")
    plt.ylabel("Rain in mm")
    plt.plot(date_list, rain, marker="o", color = "b")
    plt.show()
    return (rain)    
    



#--------------------------------------------------------#