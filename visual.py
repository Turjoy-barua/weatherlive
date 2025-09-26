import fetch
import datetime 
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def date():
    
    pass

def temp_trend():
    temp = []
    feels_like = []
    humidity = []
    date = []
    today = datetime.datetime.now()
    day = today.day
    while day >= (today.day - 20):
        data = fetch.fetch_24(today.year, today.month, day, "paris")
        date.append(day)
        temp.append(kel_to_c(data["data"][0]["temp"]))
        feels_like.append(kel_to_c(data["data"][0]["feels_like"]))
        humidity.append(data["data"][0]["humidity"])
        # rain = data["data"][0]["weather"] --> to be done
        
        day-=1
    temp.reverse()
    
    print(date)
    print(temp)
    print(feels_like)
    print(humidity)
    """ plt.suptitle("Temperature trend of last 7 days")
    plt.xlabel("date")
    plt.ylabel("Temperature")
    plt.plot(date,temp)
    plt.show()    """     

temp_trend()



#--------------------------------------------------------#
""" import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show() """