


""" import streamlit as st
import pandas as pd
import time

d = {
    'dates': [0,1,2,3,4,5,6,7,8,9],
    'temp': [10,20,30,20,40,50,60,70,80,80],
    'humidity': [10,20,30,40,50,60,70,80,90,80],
    'rain': [10,20,2,30,40,50,60,70,80,80]
}
df = pd.DataFrame(data=d)
total_days = len(df)

progress_text = "Operation in progress. Please wait."

st.line_chart(df[['dates', 'temp']].set_index('dates'))
st.line_chart(df[['dates', 'humidity']].set_index('dates'))
st.line_chart(df[['dates', 'rain']].set_index('dates'))

my_bar = st.progress(0, text=progress_text)

for i in range(total_days):
    time.sleep(0.1)  
    percent_complete = int((i + 1) / total_days * 100)  
    my_bar.progress(percent_complete, text=progress_text)

my_bar.empty()  
st.success("Done!") """