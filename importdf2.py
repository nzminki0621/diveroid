import pandas as pd
import numpy as np
from datetime import datetime as dt 
import datetime
import timezone as tz
from importdf import timeplus, timeplus_world, divide_by_mil, df_proc, df_us
from importdf import df10, df11, df12, df13, df14, df15, df_all

us_all = df_us(df_all)

us10 = df_us(df10)
us11 = df_us(df11)
us12 = df_us(df12)
us13 = df_us(df13)
us14 = df_us(df14)
us15 = df_us(df15)