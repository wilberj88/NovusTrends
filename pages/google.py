import streamlit as st
import pytrends
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pytrends.request import TrendReq


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="⚙️")

st.title('Novus Trends ⚙️')
st.header("Monitores de Tendencias en Google en tiempo real💹")

pytrends = TrendReq(hl='en-US', tz=360)
st.write("Tendencias Hoy en Estados Unidos 🇺🇸")
# Google Trends data
df1 = pytrends.trending_searches(pn='united_states')
st.dataframe(df1.head(10))


st.write("Tendencias Hoy en Colombia 🇨🇴")
# Google Trends data
df3 = pytrends.trending_searches(pn='colombia')
st.dataframe(df3.head(10))

st.write("Tendencias Hoy en Reino Unido 🇬🇧")
# Google Trends data
df5 = pytrends.trending_searches(pn='united_kingdom')
st.dataframe(df5.head(10))

st.write("Tendencias Hoy en Nigeria 🇳🇬")
# Google Trends data
df4 = pytrends.trending_searches(pn='nigeria')
st.dataframe(df4.head(10))

#st.write("Tendencias Hoy en España 🇪🇸")
# Google Trends data
#df2 = pytrends.trending_searches(pn='españa')
#st.dataframe(df2.head(10))


#GetRealTime Google Search Trends
st.write("Tendencias Hoy")
dfhottoday = pytrends.today_searches()
st.dataframe(dfhottoday.head(10))

