import streamlit as st
import pytrends
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="📈")

st.title('Novus Trends 📈')
st.header("Monitores de Tendencias en tiempo real💹")

st.write("Bienvenidos al futuro de las alarmas y recomendaciones automáticas basadas en Tendencias 🧭")

st.markdown(
  """
  En esta web encontrarás:
  - 🔎_    Monitor de Tendencia en Google
  - 🛒_    Monitor de Tendencia en Twitter
  - 🧾_    Monitor de Tendencia en Microsoft-BING
  
  Con la tecnología de Novus Trends 📈 podrás:
  - Monitorizar Sentimientos en Redes Sociales
  - Monitorizar Tendencias de Mercado en Search Engines
  - Monitorizar la oferta de la competencia
  - Monitorizar la información de gobiernos, noticias, entre otros
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)
