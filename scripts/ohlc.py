
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from datetime import datetime


# In[3]:


import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:4KS5CJlz0ZX8Po@localhost:5432/postgres')


# In[4]:


#10000 record test table
df = pd.read_sql_query("select * from merged limit 10000;", engine)
# df = pd.read_sql_query("select * from merged;", engine)


# In[5]:


df = df.set_index(pd.DatetimeIndex(df['timestamp']))


# In[6]:


df.head()


# In[12]:


#15 MIN
fifteen_min_summary = pd.DataFrame()

fifteen_min_summary['open'] = df.open.resample('15T').first().ffill()
fifteen_min_summary['high'] = df.high.resample('15T').max().ffill()
fifteen_min_summary['low'] = df.low.resample('15T').min().ffill()
fifteen_min_summary['close'] = df.close.resample('15T').last().ffill()

fifteen_min_summary["interval"] = df.ix[4, 'interval'] = '15m'

# fifteen_min_summary.head()
fifteen_min_summary.to_sql('fifteen_min_summary', engine, if_exists='replace')


# In[14]:


#1 HR
hourly_summary = pd.DataFrame()

hourly_summary['open'] = df.open.resample('H').first().ffill()
hourly_summary['high'] = df.high.resample('H').max().ffill()
hourly_summary['low'] = df.low.resample('H').min().ffill()
hourly_summary['close'] = df.close.resample('H').last().ffill()

hourly_summary["interval"] = df.ix[4, 'interval'] = '1H'

# hourly_summary.head()
hourly_summary.to_sql('hourly_summary', engine, if_exists='replace')


# In[15]:


#4 HR
four_hr_summary = pd.DataFrame()

four_hr_summary['open'] = df.open.resample('4H').first().ffill()
four_hr_summary['high'] = df.high.resample('4H').max().ffill()
four_hr_summary['low'] = df.low.resample('4H').min().ffill()
four_hr_summary['close'] = df.close.resample('4H').last().ffill()

four_hr_summary["interval"] = df.ix[4, 'interval'] = '4H'

# four_hr_summary.head()
four_hr_summary.to_sql('four_hr_summary', engine, if_exists='replace')


# In[16]:


#1 DAY
day_summary = pd.DataFrame()

day_summary['open'] = df.open.resample('D').first().ffill()
day_summary['high'] = df.high.resample('D').max().ffill()
day_summary['low'] = df.low.resample('D').min().ffill()
day_summary['close'] = df.close.resample('D').last().ffill()

day_summary["interval"] = df.ix[4, 'interval'] = '1D'

# day_summary.head()
day_summary.to_sql('day_summary', engine, if_exists='replace')


# In[17]:


#1 week
weekly_summary = pd.DataFrame()

weekly_summary['open'] = df.open.resample('W').first().ffill()
weekly_summary['high'] = df.high.resample('W').max().ffill()
weekly_summary['low'] = df.low.resample('W').min().ffill()
weekly_summary['close'] = df.close.resample('W').last().ffill()

weekly_summary["interval"] = df.ix[4, 'interval'] = '1W'

# weekly_summary.head()
weekly_summary.to_sql('weekly_summary', engine, if_exists='replace')


# In[18]:


#1 MO
month_summary = pd.DataFrame()

month_summary['open'] = df.open.resample('M').first().ffill()
month_summary['high'] = df.high.resample('M').max().ffill()
month_summary['low'] = df.low.resample('M').min().ffill()
month_summary['close'] = df.close.resample('M').last().ffill()

month_summary["interval"] = df.ix[4, 'interval'] = '1M'

# month_summary.head()
month_summary.to_sql('month_summary', engine, if_exists='replace')


# In[19]:


#1 YR

yearly_summary = pd.DataFrame()

yearly_summary['open'] = df.open.resample('AS').first().ffill()
yearly_summary['high'] = df.high.resample('AS').max().ffill()
yearly_summary['low'] = df.low.resample('AS').min().ffill()
yearly_summary['close'] = df.close.resample('AS').last().ffill()

yearly_summary["interval"] = df.ix[4, 'interval'] = '1Y'

# yearly_summary.head()
yearly_summary.to_sql('yearly_summary', engine, if_exists='replace')

