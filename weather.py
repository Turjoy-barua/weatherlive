import streamlit as st
import matplotlib as plt
import main
st.title(":red[WEATHERLIVE APP]")
page_element="""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1743341942781-14f3c65603c4?q=80&w=5342&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)


top_overview_cont = st.container(border=True)
user_input = top_overview_cont.text_input("Enter the city")
if user_input:
    city = user_input

location, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm , description = main.current_weather('paris')
    

today_comment = st.container(border=True)
today_comment.write("todays weathe")



overview_cont = st.container(border=True, horizontal_alignment="center")
overview_cont.title("Current Weather",)
location_column, date_column = st.columns(2)
location_column.header(f'Location : {location}')
date_column.header(f'Date : {date}')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f"{temp} °C")
col1.write(f"\tFeels like{fl}")
col2.metric("Humidity", f"{humidity} %")
col3.metric("Rain", f"{rain_mm} mm")



details_cont = st.container(border=True)
details_cont_col1, details_cont_col2 = st.columns(2)
details_cont_col1.metric("SUNRISE", sunrise)
details_cont.divider(width="stretch")
details_cont_col1.metric("SUNSET", sunset)
details_cont_col1.metric("Uvi Index", uvi)
details_cont_col2.metric("")





