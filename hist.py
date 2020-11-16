import pandas as pd
import numpy as np
from datetime import datetime as dt 
import datetime
import time
import matplotlib.pyplot as plt
from scipy import stats
import timezone as tz
import seaborn as sns

def divide_by_mil(i):
    return i/1000000
def divide_by_bil(i):
    return i/1000000000
def just_time(str):
    return str[-8:]

def timeplus(row):
    try:
        return row.datetime64 + datetime.timedelta(hours=tz.us_time[row.geo_region])
    except:
        return row.datetime64
def ticks_double(list):
    new_list = []
    for i in range(len(list)-1):
        new_list.append((list[i]+list[i+1])/2)
    double_list = []
    for i in range(len(list)):
        double_list.append(list[i])
        try:
            double_list.append(new_list[i])
        except:
            pass
    return double_list

def us_visit_click(df):
    us = df[df.geo_country == 'United States'].reset_index(drop=True)
    us['human_time'] = us.apply(timeplus, axis=1)   #미국 시간대 보정
    us = us.dropna(subset = ['geo_region'])
    first_visit = us[us.event_name == 'first_visit' ]
    click_target = us[us.event_name == 'click_target' ]
    plt.figure(figsize=(20,5))
    plt.subplot()

    plt.hist(first_visit.human_time.astype('datetime64'),histtype = 'barstacked', bins=40)
    plt.hist(click_target.human_time.astype('datetime64'),histtype = 'barstacked', bins=40)
    return None

def visit_click(df):
    first_visit = df[df.event_name == 'first_visit' ]
    click_target = df[df.event_name == 'click_target' ]
    plt.figure(figsize=(20,10))
    plt.subplot(2,1,1)

    plt.hist(first_visit.human_time.astype('datetime64'),histtype = 'barstacked', bins=40)
    plt.hist(click_target.human_time.astype('datetime64'),histtype = 'barstacked', bins=40)

    plt.subplot(2,1,2)
    sns.kdeplot(first_visit.human_time.astype(np.int64), label = 'first_visit')
    sns.kdeplot(click_target.human_time.astype(np.int64), label = 'click_target')
    plt.xticks(plt.xticks()[0],labels = pd.Series(plt.xticks()[0]).map(divide_by_bil).map(dt.fromtimestamp).map(np.datetime64))
    return None

def kde_plot(df):
    first_visit = df[df.event_name == 'first_visit' ]
    click_target = df[df.event_name == 'click_target' ]
    plt.figure(figsize = (20,5))
    sns.kdeplot(first_visit.human_time.astype(np.int64), label = 'first_visit')
    sns.kdeplot(click_target.human_time.astype(np.int64), label = 'click_target')
    plt.xticks(plt.xticks()[0],labels = pd.Series(plt.xticks()[0]).map(divide_by_bil).map(dt.fromtimestamp).map(np.datetime64))
