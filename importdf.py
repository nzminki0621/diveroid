import pandas as pd
import numpy as np
from datetime import datetime as dt 
import datetime
import timezone as tz

def timeplus(row):
    try:
        return row.datetime64 + datetime.timedelta(hours=tz.us_time[row.geo_region])
    except:
        return row.datetime64

def divide_by_mil(i):
    return i/1000000

def df_proc(df):
    df['datetime64'] = df.event_timestamp.map(int).map(divide_by_mil).map(dt.fromtimestamp).map(np.datetime64)
    df['human_time'] = df['datetime64']
    first_visit = df[df.event_name == 'first_visit']
    click_target = df[df.event_name == 'click_target']
    return df, first_visit, click_target

def df_us(df):
    us = df[df.geo_country == 'United States'].reset_index(drop=True)
    us['human_time'] = us.apply(timeplus, axis=1)   #미국 시간대 보정
    us = us.dropna(subset = ['geo_region'])
    us_first_visit = us[us.event_name == 'first_visit' ]
    us_click_target = us[us.event_name == 'click_target' ]
    return us, us_first_visit, us_click_target



df_all = pd.concat([pd.read_csv('20201110.csv'),pd.read_csv('20201111.csv'),pd.read_csv('20201112.csv'),pd.read_csv('20201113.csv')])
df_all, df_first_visit, df_click_target = df_proc(df_all)
us_all, us_first_visit, us_click_target = df_us(df_all)

df10 = pd.read_csv('20201110.csv')
df10, df10_first_visit, df10_click_target = df_proc(df10)
us10, us10_first_visit, us10_click_target = df_us(df10)

df11 = pd.read_csv('20201111.csv')
df11, df11_first_visit, df11_click_target = df_proc(df11)
us11, us11_first_visit, us11_click_target = df_us(df11)

df12 = pd.read_csv('20201112.csv')
df12, df12_first_visit, df12_click_target = df_proc(df12)
us12, us12_first_visit, us12_click_target = df_us(df12)

df13 = pd.read_csv('20201113.csv')
df13, df13_first_visit, df13_click_target = df_proc(df13)
us13, us13_first_visit, us13_click_target = df_us(df13)