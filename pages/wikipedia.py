import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

url = "https://es.wikipedia.org/wiki/Wikipedia:Efem%C3%A9rides"
page = requests.get(url)
soup = BeautifulSoup(page.content , 'html.parser')

def get_soup(url):
    # Page content from Website URL
    page = requests.get(url)
    
    # parse html content
    soup = BeautifulSoup(page.content , 'html.parser')

    return soup


def get_paragraph_text(p):
    paragraph_text = ''
    for tag in p.children:
        paragraph_text = paragraph_text + tag.text
    
    return paragraph_text
    
def clean_wiki_content(text):
    text = re.sub("\[\d+\]", "" , text)
    text = text.replace("[edit]", "")
    return text
