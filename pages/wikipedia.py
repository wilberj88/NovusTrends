import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://es.wikipedia.org/wiki/Wikipedia:Efem%C3%A9rides"
def get_soup(url):
    # Page content from Website URL
    page = requests.get(url)
    
    # parse html content
    soup = BeautifulSoup(page.content , 'html.parser')
    return soup
def clean_wiki_content(text):
    text = re.sub("\[\d+\]", "" , text)
    text = text.replace("[edit]", "")
    return text
def get_paragraph_text(p):
    paragraph_text = ''
    for tag in p.children:
        paragraph_text = paragraph_text + tag.text
    
    return paragraph_text
def get_wiki_extract(url):
    soup = get_soup(url) 
    headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    wiki_extract = []
    for tag in soup.find_all():
        if tag.name in headers and tag.text != 'Contents':
            # We try to find all paragraphs after it
            p = ''
            # loop through the next elements
            for ne in tag.next_elements:
                if ne.name == 'p':
                    p = p + get_paragraph_text(ne)
                if ne.name in headers:
                    break
            if p != '':
                section = [clean_wiki_content(tag.text), tag.name, clean_wiki_content(p)]
                wiki_extract.append(section)
        
    return wiki_extract
    
    
wiki_extract = get_wiki_extract(url)
st.write(wiki_extract)
