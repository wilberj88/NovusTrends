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

st.write("Elige tendencia y ubicación. Nuestra tecnología hará el resto")

st.markdown(
  """
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)

pytrends = TrendReq(hl='en-US', tz=360)
keyword_list = ['buy home']
pytrends.build_payload(keyword_list, cat=0, timeframe='today 12-m')

# Google Trends data
df = pytrends.trending_searches(pn='nigeria')
st.dataframe(df.head(10))
