import streamlit as st
import main
import pandas as pd


st.title(":red[WEATHERLIVE APP]")
page_element="""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1477346611705-65d1883cee1e?q=80&w=3540&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

st.set_page_config( # --> configuring the page
    page_title="weatherlive",
    page_icon="🌦️",
    layout="wide",
)

left_part, right_part = st.columns(2)
top_overview_cont = left_part.container(border=True)
user_input = top_overview_cont.text_input("Enter the city")



if user_input:
    try:
        location, country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm , description , total_daytime, current_time_loc = main.current_weather(user_input) #"paris", "france", "11/10/2025", '07:55:57', '19:22:02', 15.2 , 14.5, 1021, 69, 9.5, 0.32, 40, 100000, 9.26, 0, 'SCATTERED CLOUDS', 0 , 0
            
        # --> basic overview container
        overview_cont = top_overview_cont.container(border=True, horizontal_alignment="center")
        overview_cont.title("Current Weather",)
        location_column, date_time_column = overview_cont.columns(2)
        location_column.subheader(f'Location : {location}, {country}')
        date_col, time_col = date_time_column.columns(2)
        date_col.subheader(f'Date : {date}')
        time_col.write("")
        time_col.write(f"**Current time in location: {current_time_loc}**")

        col1, col2 = overview_cont.columns(2)
        
        col1.title(f" {main.weather_emoji(description)}    {temp} °C")
        col1.subheader(f"{description.upper()}")

        col2.write("")
        feels_like_cont = col2.container(border=True)
        feels_like_cont.markdown(f":green[**Feels like {fl} °C**]", width="stretch")

        # --> details container 

        details_cont = top_overview_cont.container(border=True)
        details_cont.write("OVERVIEW")
        details_cont_col1, details_cont_col2 = details_cont.columns(2)
        details_cont_col1.metric("Rain", f"{rain_mm} mm")
        details_cont_col1.metric("Uvi Index", uvi)
        details_cont_col1.metric("wind", f"{wind_speed} km/h")
        details_cont_col1.metric("Humidity", f"{humidity}%")
        details_cont_col2.metric("dew Point", f"{dew_point} °C")
        details_cont_col2.metric("Pressure", f"{pressure} mb")
        details_cont_col2.metric("cloud cover", f"{clouds}%")
        details_cont_col2.metric("visibility", f"{visibility} km")

        # --> total daytime container
        sun_cont = top_overview_cont.container(border=True)
        hours = int(total_daytime // 3600)
        minutes = int((total_daytime % 3600) // 60)
        seconds = int(total_daytime % 60)
        sun_col1, sun_col2 = sun_cont.columns(2)
        sun_col1.write("DAYTIME")
        sun_col1.write("")
        sun_col1.write("")
        sun_col1.subheader(f"☀️  {hours}hrs {minutes}min {seconds}sec")
        sun_col2.metric("Sunrise", sunrise)
        sun_col2.metric("Sunset", sunset)
        
        # --> graph container
        right_upper_part = right_part.container(border=True)
        right_upper_part.subheader("Graph of last 20 days")
        temp_graph = right_upper_part.container(border=True)
        humidity_graph = right_upper_part.container(border=True)
        rain_graph = right_upper_part.container(border=True) #graph_values.trend(user_input)
        d = {'dates': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'temp': [10, 20, 30, 20, 40, 50, 60, 70, 80, 80], 'humidity': [10, 20, 30, 40, 50, 60, 70, 80, 90, 80], 'rain': [10, 20, 2, 30, 40, 50, 60, 70, 80, 80]}
        df = pd.DataFrame(data=d)
        total_days = len(df)
        progress_text = "Operation in progress. Please wait."

        temp_graph.line_chart(df, x='dates', y='temp')
        humidity_graph.line_chart(df, x ="dates", y="humidity")
        rain_graph.line_chart(df, x='dates', y='rain')
        
    except Exception as error: # --> if the api returns an error cause of wrong input or whatever
        st.title("Can't find the city")
else:
    st.write("search a city weather")


