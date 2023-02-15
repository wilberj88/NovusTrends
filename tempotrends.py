google_trends
google_trends.head()

cal = calendar()
holidays = cal.holidays(start = google_trends['date'].min(), end = google_trends['date'].max())
google_trends['holiday'] = google_trends['date'].isin(holidays)
google_trends['holiday'] = google_trends['holiday'].apply(lambda x: 1 if x == True else 0)
google_trends.head()

# Getting the day of the week
google_trends['d'] = google_trends['date'].dt.dayofweek

# Creating is_weekday variable
google_trends['is_weekday'] = google_trends['d'].apply(lambda x: 1 if x != 5 and x !=6 else 0)

# Creating is_weekend variable
google_trends['is_weekend'] = google_trends['d'].apply(lambda x: 1 if x == 5 or x == 6 else 0)
google_trends.head()

google_trends['d'] = google_trends['d'].apply(lambda x: 'monday' if x == 0 else
                              'tuesday' if x == 1 else
                              'wednesday' if x == 2 else
                              'thursday' if x == 3 else
                              'friday' if x == 4 else
                              'saturday' if x == 5 else
                              'sunday' if x == 6
                    else x)

google_trends
