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

st.write("Tendencias Hoy en Estados Unidos 🇺🇸")
# Google Trends data
df = pytrends.trending_searches(pn='united_states')
st.dataframe(df.head(10))

st.write("Tendencias Hoy en Nigeria 🇳🇬")
# Google Trends data
df = pytrends.trending_searches(pn='nigeria')
st.dataframe(df.head(10))
