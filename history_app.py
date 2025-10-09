import streamlit as st
import database as db

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
st.set_page_config(
    page_title="weatherlive",
    page_icon="🌦️",
    layout="wide",
)


df = pd.DataFrame()