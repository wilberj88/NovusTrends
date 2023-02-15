import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import numpy as np
import datetime as dt
from datetime import date
from pytrends.request import TrendReq
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import matplotlib.pyplot as plt

import warnings

# Notebook settings
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', None)
pytrends = TrendReq(hl='en-US', tz=360)
# sns.set_theme()

kw_list = ['covid']
frequency = 'daily' # ie. hourly, weekly, monthly, yearly
geo = 'US'
hl='en-US'

# Select Start Date
year_start = 2020
month_start = 1
day_start=1
hour_start=0

# Select End Date
year_end=2022
month_end=5
day_end=15
hour_end=0

# Run PyTrends
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
                                 gprop='', 
                                 sleep=0,
                                 frequency=frequency)


google_trends = google_trends.reset_index()
google_trends.columns = ['date', 'keyword','partial']
google_trends.drop(['partial'], axis=1, inplace=True)
pd.to_datetime(google_trends['date'])

google_trends.head()


sns.set(rc={"figure.figsize":(14, 6)})

sns.lineplot(data=google_trends, x='date', y='keyword')
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Google Trends', fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.savefig("google_trend_plot.png", dpi=360, bbox_inches='tight')
plt.show()

# Plot google trends over time
sns.set(rc={"figure.figsize":(14, 4)})

sns.lineplot(data=google_trends, x='date', y='keyword')
plt.xlabel('Date')
plt.ylabel('Google Trends')
# plt.savefig("google_trend_plot.jpg", dpi=360, bbox_inches='tight')
plt.show()

# Save Google Trends file
today = date.today()
d1 = today.strftime("%d-%m-%Y")
google_trends.to_csv('google_trends_'+kw_list[0]+'_'+ d1+'.csv')

# Get Google Keyword Suggestions
#pytrend = TrendReq()
#keywords = pytrend.suggestions(keyword='buy house')
#df = pd.DataFrame(keywords)
#df
