import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import pandas as pd


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus MANDO Trends", page_icon="🎮")

st.title('Novus MANDO 🎮')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.header('Tendencias y Climas Mundiales 🌎')

colored_header(
    label="Búsquedas online en Google",
    description="Última hora y día",
    color_name="violet-70",
)

pytrends = TrendReq(hl='en-US', tz=360)
col4, col5, col6 = st.columns(3)
with col4:
    st.write("🇺🇸 USA Top10 Trending Search in last hour")
      # Google Trends data
    df1 = pytrends.trending_searches(pn='US')
    st.dataframe(df1.head(10))
with col5:
    st.write("🇬🇧 UK Top10 Trending Search in last hour")
      # Google Trends data
    df2 = pytrends.trending_searches(pn='united_kingdom')
    st.dataframe(df2.head(10))
with col6:
    st.write("🇨🇴 COL Top10 Trending Search in last hour")
    df3 = pytrends.trending_searches(pn='colombia')
    st.dataframe(df3.head(10))
    




colored_header(
    label="Wheater Now",
    description="América, EU & ASIA",
    color_name="red-70",
)

#ALARMS CONFIGURATION
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
sity1 = "New York"
sity2 = "San Francisco"
sity3 = "Toledo"
sity4 = "London"
sity5 = "Pekin"
sity6 = "Bombai"
URL1 = BASE_URL + "q=" + sity1 + "&appid=" + API_KEY
URL2 = BASE_URL + "q=" + sity2 + "&appid=" + API_KEY
URL3 = BASE_URL + "q=" + sity3 + "&appid=" + API_KEY
URL4 = BASE_URL + "q=" + sity4 + "&appid=" + API_KEY
URL5 = BASE_URL + "q=" + sity5 + "&appid=" + API_KEY
URL6 = BASE_URL + "q=" + sity6 + "&appid=" + API_KEY


response1 = requests.get(URL1)
response2 = requests.get(URL2)
response3 = requests.get(URL3)
response4 = requests.get(URL4)
response5 = requests.get(URL5)
response6 = requests.get(URL6)

if response1.status_code == 200:
   # getting data in the json format
   data1 = response1.json()
   # getting the main dict block
   main1 = data1['main']
  # getting temperature
   temperature1 = main1['temp']
   # getting the humidity
   humidity1 = main1['humidity']
   # getting the pressure
   pressure1 = main1['pressure']
   # weather report
   report1 = data1['weather']

if response2.status_code == 200:
   # getting data in the json format
   data2 = response2.json()
   # getting the main dict block
   main2 = data2['main']
  # getting temperature
   temperature2 = main2['temp']
   # getting the humidity
   humidity2 = main2['humidity']
   # getting the pressure
   pressure2 = main2['pressure']
   # weather report
   report2 = data2['weather']

if response3.status_code == 200:
   # getting data in the json format
   data3 = response3.json()
   # getting the main dict block
   main3 = data3['main']
  # getting temperature
   temperature3 = main3['temp']
   # getting the humidity
   humidity3 = main3['humidity']
   # getting the pressure
   pressure3 = main3['pressure']
   # weather report
   report3 = data3['weather']

if response4.status_code == 200:
   # getting data in the json format
   data4 = response4.json()
   # getting the main dict block
   main4 = data4['main']
  # getting temperature
   temperature4 = main4['temp']
   # getting the humidity
   humidity4 = main4['humidity']
   # getting the pressure
   pressure4 = main4['pressure']
   # weather report
   report4 = data4['weather']

if response5.status_code == 200:
   # getting data in the json format
   data5 = response5.json()
   # getting the main dict block
   main5 = data5['main']
  # getting temperature
   temperature5 = main5['temp']
   # getting the humidity
   humidity5 = main5['humidity']
   # getting the pressure
   pressure5 = main5['pressure']
   # weather report
   report5 = data5['weather']

if response6.status_code == 200:
   # getting data in the json format
   data6 = response6.json()
   # getting the main dict block
   main6 = data6['main']
  # getting temperature
   temperature6 = main6['temp']
   # getting the humidity
   humidity6 = main6['humidity']
   # getting the pressure
   pressure6 = main6['pressure']
   # weather report
   report6 = data6['weather']

col4, col5, col6 = st.columns(3)

with col4:
    st.write("🌧 USA ☀️")
    st.write(f"{sity1:-^30}")
    st.write(f"Temperature (Kelvins): {temperature1}")
    st.write(f"Humidity: {humidity1}")
    st.write(f"Pressure: {pressure1}")
    st.write(f"Weather Report: {report1[0]['description']}")
    st.write(f"{sity2:-^30}")
    st.write(f"Temperature (Kelvins): {temperature2}")
    st.write(f"Humidity: {humidity2}")
    st.write(f"Pressure: {pressure2}")
    st.write(f"Weather Report: {report2[0]['description']}")

with col5:
    st.write("🌧 Europe ☀️")
    st.write(f"{sity3:-^30}")
    st.write(f"Temperature (Kelvins): {temperature3}")
    st.write(f"Humidity: {humidity3}")
    st.write(f"Pressure: {pressure3}")
    st.write(f"Weather Report: {report3[0]['description']}")
    st.write(f"{sity4:-^30}")
    st.write(f"Temperature (Kelvins): {temperature4}")
    st.write(f"Humidity: {humidity4}")
    st.write(f"Pressure: {pressure4}")
    st.write(f"Weather Report: {report4[0]['description']}")
    
with col6:
    st.write("🌧 Asia ☀️")
    st.write(f"{sity5:-^30}")
    st.write(f"Temperature (Kelvins): {temperature5}")
    st.write(f"Humidity: {humidity5}")
    st.write(f"Pressure: {pressure5}")
    st.write(f"Weather Report: {report5[0]['description']}")
    st.write(f"{sity6:-^30}")
    st.write(f"Temperature (Kelvins): {temperature6}")
    st.write(f"Humidity: {humidity6}")
    st.write(f"Pressure: {pressure6}")
    st.write(f"Weather Report: {report6[0]['description']}")
    





