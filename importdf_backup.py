import pandas as pd
import numpy as np
from datetime import datetime as dt 
import datetime
import timezone as tz

def timeplus(row):
    try:
        return row.datetime64 + datetime.timedelta(hours=tz.us_time[row.geo_region])
    except:
        return row.human_time

def timeplus_world(row):
    try:
        return row.datetime64 + datetime.timedelta(hours=tz.world_time[row.geo_country])
    except:
        return row.human_time

def divide_by_mil(i):
    return i/1000000

def df_proc(df):
    df['datetime64'] = df.event_timestamp.map(int).map(divide_by_mil).map(dt.fromtimestamp).map(np.datetime64)
    df['human_time'] = df['datetime64']
    df['human_time'] = df.apply(timeplus_world, axis=1)   #세계 시간대 보정
    df['human_time'] = df.apply(timeplus, axis=1)   #미국 시간대 보정
    first_visit = df[df.event_name == 'first_visit']
    click_target = df[df.event_name == 'click_target']
    return df, first_visit, click_target

def df_us(df):
    us = df[df.geo_country == 'United States'].reset_index(drop=True)
    us = us.dropna(subset = ['geo_region'])
    us_first_visit = us[us.event_name == 'first_visit' ]
    us_click_target = us[us.event_name == 'click_target' ]
    return us, us_first_visit, us_click_target



df_all = pd.concat([pd.read_csv('20201110.csv'),pd.read_csv('20201111.csv'),pd.read_csv('20201112.csv'),pd.read_csv('20201113.csv'),pd.read_csv('20201114.csv'),pd.read_csv('20201115.csv')])
df_all, df_first_visit, df_click_target = df_proc(df_all)


df10 = pd.read_csv('20201110.csv')
df10, df10_first_visit, df10_click_target = df_proc(df10)

df11 = pd.read_csv('20201111.csv')
df11, df11_first_visit, df11_click_target = df_proc(df11)

df12 = pd.read_csv('20201112.csv')
df12, df12_first_visit, df12_click_target = df_proc(df12)

df13 = pd.read_csv('20201113.csv')
df13, df13_first_visit, df13_click_target = df_proc(df13)

df14 = pd.read_csv('20201114.csv')
df14, df14_first_visit, df14_click_target = df_proc(df14)

df15 = pd.read_csv('20201115.csv')
df15, df15_first_visit, df15_click_target = df_proc(df15)