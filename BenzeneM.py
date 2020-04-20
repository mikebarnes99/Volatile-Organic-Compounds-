import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime
import matplotlib.dates as mdates

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read the data
db97 = pd.read_csv(r'/Users/Henry/Desktop/1997 VOC data.csv')
db98 = pd.read_csv(r'/Users/Henry/Desktop/1998 VOC data.csv')
db99 = pd.read_csv(r'/Users/Henry/Desktop/1999 VOC data.csv')
db00 = pd.read_csv(r'/Users/Henry/Desktop/2000 VOC data.csv')
db01 = pd.read_csv(r'/Users/Henry/Desktop/2001 VOC data.csv')
db02 = pd.read_csv(r'/Users/Henry/Desktop/2002 VOC data.csv')
db03 = pd.read_csv(r'/Users/Henry/Desktop/2003 VOC data.csv')
db04 = pd.read_csv(r'/Users/Henry/Desktop/2004 VOC data.csv')
db05 = pd.read_csv(r'/Users/Henry/Desktop/2005 VOC data.csv')
db06 = pd.read_csv(r'/Users/Henry/Desktop/2006 VOC data.csv')
db07 = pd.read_csv(r'/Users/Henry/Desktop/2007 VOC data.csv')
db08 = pd.read_csv(r'/Users/Henry/Desktop/2008 VOC data.csv')
db09 = pd.read_csv(r'/Users/Henry/Desktop/2009 VOC data.csv')
db11 = pd.read_csv(r'/Users/Henry/Desktop/2011 VOC data.csv')
db12 = pd.read_csv(r'/Users/Henry/Desktop/2012 VOC data.csv')
db13 = pd.read_csv(r'/Users/Henry/Desktop/2013 VOC data.csv')
db14 = pd.read_csv(r'/Users/Henry/Desktop/2014 VOC data.csv')
db15 = pd.read_csv(r'/Users/Henry/Desktop/2015 VOC data.csv')
db17 = pd.read_csv(r'/Users/Henry/Desktop/2017 VOC data.csv')
db18 = pd.read_csv(r'/Users/Henry/Desktop/2018 VOC data.csv')
db19 = pd.read_csv(r'/Users/Henry/Desktop/2019 VOC data.csv')

datasets = [db97,db98,db99,db00,db01,db02,db03,db04,db05,db06,db07,db08,db09,db11,db12,db13,db14,db15,db17,db18,db19]
#datasets = [db97]
x=[]
y=[]

for i in range(len(datasets)):

    Date = datasets[i]['Date']

    voc = datasets[i].iloc[:,170]

    # Remove No data 
    A = voc[voc!='No data']

    # Find indices of the rows with no data
    B = voc[voc == 'No data'].index.tolist()

    # Drop those dates associated with no data
    Date = Date.drop(Date.index[B])

    # Reset the indices
    NewDate = Date.reset_index(drop=True)
    NewVOC = A.reset_index(drop=True)

    # Convert dates to format that can be plotted
    NewDate = pd.to_datetime(NewDate,dayfirst=True)
    Dates = dates.date2num(NewDate)

    # Convert data to floats
    for i in range(len(NewVOC)):
        NewVOC[i] = float(NewVOC[i])
    
    years = mdates.YearLocator(5)   # every 5 years
    #years = mdates.YearLocator()   # every year
    otheryears = mdates.YearLocator()  # other years
    months = mdates.MonthLocator() # every month
    years_fmt = mdates.DateFormatter('%Y')

    xfmt = mdates.DateFormatter('%d-%m-%y')

    # Add data to arrays to be plotted
    x.append(Dates)
    y.append(NewVOC)
    
fig, ax = plt.subplots(figsize=(10.5,6))
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(otheryears)

for i in range(len(x)):
    #plt.plot_date(x[i],y[i],color='blue')
    plt.plot(x[i],y[i],c='#1f77b4')
#fig.autofmt_xdate()
plt.title('Benzene levels on Marylebone Road London from 1997-2020')
plt.xlabel('Time')
plt.ylabel('Micrograms per metre cubed')
plt.show()

