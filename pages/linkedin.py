import streamlit as st
import pytrends
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="⚙️")

st.title('Novus Trends ⚙️')
st.header("Monitores de Tendencias en LinkedIn en tiempo real💹")

job_name = "Data Analyst"
country_name = "United States"

job_url ="";
for item in job_name.split(" "):
    if item != job_name.split(" ")[-1]:
        job_url = job_url + item + "%20"
    else:
        job_url = job_url + item

country_url ="";
for item in country_name.split(" "):
    if item != country_name.split(" ")[-1]:
        country_url = country_url + item + "%20"
    else:
        country_url = country_url + item

url = "https://www.linkedin.com/jobs/search?keywords={0}&location={1}&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
url.format(job_url,country_url)

TIMEOUT = 20

st.title("Test Selenium")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(options=firefoxOptions)
driver.get(URL)

# Creating a webdriver instance
driver = webdriver.Chrome("ChromeDriver_Path/chromedriver")
# Opening the url we have just defined in our browser
driver.get(url)

#We find how many jobs are offered.
jobs_num = driver.find_element(By.CSS_SELECTOR,"h1>span").get_attribute("innerText")
if len(jobs_num.split(',')) > 1:
    jobs_num = int(jobs_num.split(',')[0])*1000
else:
    jobs_num = int(jobs_num)

jobs_num   = int(jobs_num)

#We create a while loop to browse all jobs. 
i = 2
while i <= int(jobs_num/2)+1:
    #We keep scrollind down to the end of the view.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    print("Current at: ", i, "Percentage at: ", ((i+1)/(int(jobs_num/2)+1))*100, "%",end="\r")
    try:
        #We try to click on the load more results buttons in case it is already displayed.
        infinite_scroller_button = driver.find_element(By.XPATH, ".//button[@aria-label='Load more results']")
        infinite_scroller_button.click()
        time.sleep(0.1)
    except:
        #If there is no button, there will be an error, so we keep scrolling down.
        time.sleep(0.1)
        pass
      
      
      
  
  
  
  #We get a list containing all jobs that we have found.
job_lists = driver.find_element(By.CLASS_NAME,"jobs-search__results-list")
jobs = job_lists.find_elements(By.TAG_NAME,"li") # return a list

#We declare void list to keep track of all obtaind data.
job_title_list = []
company_name_list = []
location_list = []
date_list = []
job_link_list = []

#We loof over every job and obtain all the wanted info.
for job in jobs:
    #job_title
    job_title = job.find_element(By.CSS_SELECTOR,"h3").get_attribute("innerText")
    job_title_list.append(job_title)
    
    #company_name
    company_name = job.find_element(By.CSS_SELECTOR,"h4").get_attribute("innerText")
    company_name_list.append(company_name)
    
    #location
    location = job.find_element(By.CSS_SELECTOR,"div>div>span").get_attribute("innerText")
    location_list.append(location)
    
    #date
    date = job.find_element(By.CSS_SELECTOR,"div>div>time").get_attribute("datetime")
    date_list.append(date)
    
    #job_link
    job_link = job.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
    job_link_list.append(job_link)
    
    
    
  
  
  
jd = [] #job_description
seniority = []
emp_type = []
job_func = []
job_ind = []
for item in range(len(jobs)):
    print(item)
    job_func0=[]
    industries0=[]
    # clicking job to view job details
    
    #__________________________________________________________________________ JOB Link
    
    try: 
        job_click_path = f'/html/body/div/div/main/section/ul/li[{item+1}]'
        job_click = job.find_element(By.XPATH,job_click_path).click()
    except:
        pass
    #job_click = job.find_element(By.XPATH,'.//a[@class="base-card_full-link"]')
    
    #__________________________________________________________________________ JOB Description
    jd_path = '/html/body/div/div/section/div/div/section/div/div/section/div'
    try:
        jd0 = job.find_element(By.XPATH,jd_path).get_attribute('innerText')
        jd.append(jd0)
    except:
        jd.append(None)
        pass
    
    #__________________________________________________________________________ JOB Seniority
    seniority_path='/html/body/div/div/section/div/div/section/div/ul/li[1]/span'
    
    try:
        seniority0 = job.find_element(By.XPATH,seniority_path).get_attribute('innerText')
        seniority.append(seniority0)
    except:
        seniority.append(None)
        pass

    #__________________________________________________________________________ JOB Time
    emp_type_path='/html/body/div/div/section/div/div/section/div/ul/li[2]/span'
    
    try:
        emp_type0 = job.find_element(By.XPATH,emp_type_path).get_attribute('innerText')
        emp_type.append(emp_type0)
    except:
        emp_type.append(None)
        pass
    
    #__________________________________________________________________________ JOB Function
    function_path='/html/body/div/div/section/div/div/section/div/ul/li[3]/span'
    
    try:
        func0 = job.find_element(By.XPATH,function_path).get_attribute('innerText')
        job_func.append(func0)
    except:
        job_func.append(None)
        pass

    #__________________________________________________________________________ JOB Industry
    industry_path='/html/body/div/div/section/div/div/section/div/ul/li[4]/span'
    
    try:
        ind0 = job.find_element(By.XPATH,industry_path).get_attribute('innerText')
        job_ind.append(ind0)
    except:
        job_ind.append(None)
        pass
    
    print("Current at: ", item, "Percentage at: ", (item+1)/len(jobs)*100, "%")

    
    
job_data = pd.DataFrame({
    'Date': date,
    'Company': company_name,
    'Title': job_title,
    'Location': location,
    'Description': jd,
    'Level': seniority,
    'Type': emp_type,
    'Function': job_func,
    'Industry': job_ind,
    'Link': job_link
})

st.dataframe(job_data)
