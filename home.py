import streamlit as st
import pytrends
from statsmodels.tsa.seasonal import seasonal_decompose


kw_list = [‘covid’]
frequency = ‘daily’ # ie. hourly, weekly, monthly, yearly
geo = ‘US’
hl=’en-US’
# Select Start Date
year_start = 2017
month_start = 6
day_start=1
hour_start=0
# Select End Date
year_end=2020
month_end=6
day_end=30
hour_end=0

google_trends = pytrends.get_historical_interest(kw_list,
 year_start = year_start, 
 month_start = month_start, 
 day_start = day_start, 
 hour_start = hour_start, 
 year_end = year_end, 
 month_end = month_end, 
 day_end = day_end, 
 hour_end = hour_end, 
 cat=0, 
 geo=geo, 
 gprop=’’, 
 sleep=0,
 frequency=frequency)
google_trends = google_trends.reset_index()
google_trends.columns = [‘date’, ‘keyword’,’partial’]
pd.to_datetime(google_trends[‘date’])
google_trends.head()

# Plot google trends over time
sns.set(rc={"figure.figsize":(14, 6)})
sns.lineplot(data=google_trends, x='date', y='keyword')

series = google_trends.set_index('date')
result = seasonal_decompose(series, model='additive', period=365)
result.seasonal.plot()
