import pandas as pd
import numpy as np
from datetime import datetime as dt 
import datetime
import timezone as tz
from importdf import timeplus, timeplus_world, divide_by_mil, df_proc, df_us
from importdf import df10, df11, df12, df13, df14, df15, df_all

def df_indo(df):
    indo = df[df.geo_country == 'Indonesia'].reset_index(drop=True)
    indo = indo.dropna(subset = ['geo_region'])
    return indo

indo_all = df_indo(df_all)

indo10 = df_indo(df10)
indo11 = df_indo(df11)
indo12 = df_indo(df12)
indo13 = df_indo(df13)
indo14 = df_indo(df14)
indo15 = df_indo(df15)