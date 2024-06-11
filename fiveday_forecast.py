import pandas as pd
import datetime as dt
from datetime import date
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt 
import numpy as np

def roundup(x, base=10):
    x = x + 10
    base = base * round(x/base)
    return base 

df_1 = pd.read_html('https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w12u=1&w13u=1&pqpfhr=6&psnwhr=6&AheadHour=4&Submit=Submit&FcstType=digital&textField1=42.5629&textField2=-83.155&site=all&unit=0&dd=&bw=')

df_2 = pd.read_html('https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w12u=1&w13u=1&pqpfhr=6&psnwhr=6&AheadHour=28&Submit=Submit&FcstType=digital&textField1=42.5629&textField2=-83.155&site=all&unit=0&dd=&bw=')

df_3 = pd.read_html('https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w12u=1&w13u=1&pqpfhr=6&psnwhr=6&AheadHour=52&Submit=Submit&FcstType=digital&textField1=42.5629&textField2=-83.155&site=all&unit=0&dd=&bw=')

df_4 = pd.read_html('https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w12u=1&w13u=1&pqpfhr=6&psnwhr=6&AheadHour=76&Submit=Submit&FcstType=digital&textField1=42.5629&textField2=-83.155&site=all&unit=0&dd=&bw=')

df_5 = pd.read_html('https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w12u=1&w13u=1&pqpfhr=6&psnwhr=6&AheadHour=100&Submit=Submit&FcstType=digital&textField1=42.5629&textField2=-83.155&site=all&unit=0&dd=&bw=')

df_1 = df_1[7]

df_2 = df_2[7]

df_3 = df_3[7]

df_4 = df_4[7]

df_5 = df_5[7]

df_1 = df_1.T

df_2 = df_2.T

df_3 = df_3.T

df_4 = df_4.T

df_5 = df_5.T

df_1 = df_1.assign(Index=range(len(df_1))).set_index('Index')
df_2 = df_2.assign(Index=range(len(df_2))).set_index('Index')
df_3 = df_3.assign(Index=range(len(df_3))).set_index('Index')
df_4 = df_4.assign(Index=range(len(df_4))).set_index('Index')
df_5 = df_5.assign(Index=range(len(df_5))).set_index('Index')

df_1 = df_1.drop(df_1.columns[0], axis=1)
df_1 = df_1.drop(df_1.columns[14:27], axis=1)
df_2 = df_2.drop(df_2.columns[0], axis=1)
df_2 = df_2.drop(df_2.columns[14:27], axis=1)
df_3 = df_3.drop(df_3.columns[0], axis=1)
df_3 = df_3.drop(df_3.columns[14:27], axis=1)
df_4 = df_4.drop(df_4.columns[0], axis=1)
df_4 = df_4.drop(df_4.columns[14:27], axis=1)
df_5 = df_5.drop(df_5.columns[0], axis=1)
df_5 = df_5.drop(df_5.columns[14:27], axis=1)

df_1.rename(columns=df_1.iloc[0], inplace = True)
df_1.drop(df_1.index[0], inplace = True)
df_2.rename(columns=df_2.iloc[0], inplace = True)
df_2.drop(df_2.index[0], inplace = True)
df_3.rename(columns=df_3.iloc[0], inplace = True)
df_3.drop(df_3.index[0], inplace = True)
df_4.rename(columns=df_4.iloc[0], inplace = True)
df_4.drop(df_4.index[0], inplace = True)
df_5.rename(columns=df_5.iloc[0], inplace = True)
df_5.drop(df_5.index[0], inplace = True)

df_1['Temperature (°F)'] = df_1['Temperature (°F)'].apply(pd.to_numeric)
df_2['Temperature (°F)'] = df_2['Temperature (°F)'].apply(pd.to_numeric)
df_3['Temperature (°F)'] = df_3['Temperature (°F)'].apply(pd.to_numeric)
df_4['Temperature (°F)'] = df_4['Temperature (°F)'].apply(pd.to_numeric)
df_5['Temperature (°F)'] = df_5['Temperature (°F)'].apply(pd.to_numeric)

df_1['Precipitation Potential (%)'] = df_1['Precipitation Potential (%)'].apply(pd.to_numeric)
df_2['Precipitation Potential (%)'] = df_2['Precipitation Potential (%)'].apply(pd.to_numeric)
df_3['Precipitation Potential (%)'] = df_3['Precipitation Potential (%)'].apply(pd.to_numeric)
df_4['Precipitation Potential (%)'] = df_4['Precipitation Potential (%)'].apply(pd.to_numeric)
df_5['Precipitation Potential (%)'] = df_5['Precipitation Potential (%)'].apply(pd.to_numeric)

day1_max_temp, day1_min_temp = df_1['Temperature (°F)'].max(), df_1['Temperature (°F)'].min()
day2_max_temp, day2_min_temp = df_2['Temperature (°F)'].max(), df_2['Temperature (°F)'].min()
day3_max_temp, day3_min_temp = df_3['Temperature (°F)'].max(), df_3['Temperature (°F)'].min()
day4_max_temp, day4_min_temp = df_4['Temperature (°F)'].max(), df_4['Temperature (°F)'].min()
day5_max_temp, day5_min_temp = df_5['Temperature (°F)'].max(), df_5['Temperature (°F)'].min()

day1_precip = df_1['Precipitation Potential (%)'].max()
day2_precip = df_2['Precipitation Potential (%)'].max()
day3_precip = df_3['Precipitation Potential (%)'].max()
day4_precip = df_4['Precipitation Potential (%)'].max()
day5_precip = df_5['Precipitation Potential (%)'].max()

day1 = (date.today() + timedelta(1)).strftime('%m-%d')
day2 = (date.today() + timedelta(2)).strftime('%m-%d')
day3 = (date.today() + timedelta(3)).strftime('%m-%d')
day4 = (date.today() + timedelta(4)).strftime('%m-%d')
day5 = (date.today() + timedelta(5)).strftime('%m-%d')

x1 = [day1, day2, day3, day4, day5]
y1 = [day1_max_temp, day2_max_temp, day3_max_temp, day4_max_temp, day5_max_temp]
y2 = [day1_min_temp, day2_min_temp, day3_min_temp, day4_min_temp, day5_min_temp]
y3 = [day1_precip, day2_precip, day3_precip, day4_precip, day5_precip]

fig = plt.figure()
ax = fig.add_subplot(111)

bar1 = ax.bar(x1, height=y1, width=0.55,align='center', color = '#EE2738', label='High')
bar2 = ax.bar(x1, height=y2, width=0.45,  align='center', color = '#448EEE', label='Low')

plt.xticks(x1)
ax.bar_label(bar1, padding=3)
ax.bar_label(bar2, padding=3)
ax.set_ylim([0,roundup(max(y1))])
ax.set_ylabel('Temperature (°F)')
ax.set_xlabel('Date')
ax.set_title('Troy, MI: Five Day Forecast')
ax.legend(loc='upper center', bbox_to_anchor=(0.20, -0.06),fancybox=True, ncol=5)
ax2 = ax.twinx()
ax2.plot(x1, y3, color = 'purple', label = 'Precip')
ax2.legend(loc='upper center', bbox_to_anchor=(0.80, -0.06),fancybox=True, ncol=5)
ax2.set_ylabel('Chance of Precipitation')
ax2.set_ylim(0, 100)
plt.tight_layout()
plt.savefig('plots/five_day_forecast.png')

