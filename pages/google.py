import streamlit as st
import pytrends
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

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

st.write("Interés por Regiones para palabra Buy")
pytrends.build_payload(kw_list=["buy"])
dfx = pytrends.interest_by_region()
st.dataframe(dfx.sort_values(by=["buy"], ascending=False))


st.write("Interés por Regiones para palabra Programming")
pytrends.build_payload(kw_list=["programming"])
dfp = pytrends.interest_by_region()
st.dataframe(dfp.sort_values(by=["programming"], ascending=False))


st.write("Top temas 2022")
dfi = pytrends.top_charts(2022, hl='en-US', tz=300, geo='GLOBAL')
st.dataframe(dfi)

st.write("Top temas 2021")
dfi = pytrends.top_charts(2021, hl='en-US', tz=300, geo='GLOBAL')
st.dataframe(dfi)

st.write("Top temas 2020")
dfi = pytrends.top_charts(2020, hl='en-US', tz=300, geo='GLOBAL')
st.dataframe(dfi)

st.write("Top temas 2019")
dfi = pytrends.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
st.dataframe(dfi)

st.write("Top Real Time temas hoy en Mundo")
dfi = pytrends.realtime_trending_searches()
st.dataframe(dfi)

st.write("Interes durante los últimos 5 años del término buy ")
kw_list= ["buy"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y')
data = pytrends.interest_over_time()
data = data.reset_index()
st.line_chart(data, x="date", y="value")
