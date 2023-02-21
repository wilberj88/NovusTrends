import streamlit as st
import pytrends
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pytrends.request import TrendReq


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="⚙️")

st.title('Novus Trends ⚙️')
st.header("Monitores de Tendencias en LinkedIn en tiempo real💹")
