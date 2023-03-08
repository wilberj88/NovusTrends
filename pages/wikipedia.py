import streamlit as st
import requests
url = "https://es.wikipedia.org/wiki/Wikipedia:Efem%C3%A9rides"
page = requests.get(url)
