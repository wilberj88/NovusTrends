import streamlit as st
import pytrends
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import schedule
import time
from datetime import datetime
from pytrends.request import TrendReq


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="⚙️")

st.title('Novus Trends USA ⚙️')
st.header("Tendencias en Google en tiempo real💹")

def job():
    pytrends = TrendReq(hl='en-US', tz=360)
    df = pytrends.trending_searches(pn='united_states')
    # Generar un nombre de archivo único por hora
    filename = 'df_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.csv'
    # Guardar el DataFrame en un archivo .csv
    df.to_csv(filename, index=False)
    st.dataframe(df.head(20))

schedule.every(1).hours.do(job)

# Bucle infinito para que el programa siga funcionando
while True:
    # Ejecutar los trabajos pendientes
    schedule.run_pending()
    # Dormir durante un segundo entre verificaciones
    time.sleep(1)
