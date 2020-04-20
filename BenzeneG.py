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
db03 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2003.csv')
db04 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2004.csv')
db05 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2005.csv')
db06 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2006.csv')
db07 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2007.csv')
db08 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2008.csv')
db09 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2009.csv')
db10 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2010.csv')
db11 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2011.csv')
db12 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2012.csv')
db13 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2013.csv')
db14 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2014.csv')
db15 = pd.read_csv(r'/Users/Henry/Desktop/Glasgow 2015.csv')

datasets = [db03,db04,db05,db06,db07,db08,db09,db10,db11,db12,db13,db14,db15]

x=[]
y=[]

for i in range(len(datasets)):

    Date = datasets[i]['Date']

    voc = datasets[i].iloc[:,16]

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
    
    years = mdates.YearLocator(1)   # every year
    #otheryears = mdates.YearLocator()  # other years
    months = mdates.MonthLocator() # every month
    years_fmt = mdates.DateFormatter('%Y')

    xfmt = mdates.DateFormatter('%d-%m-%y')

    # Add data to arrays to be plotted
    x.append(Dates)
    y.append(NewVOC)
    
fig, ax = plt.subplots(figsize=(10.5,6))
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
#ax.xaxis.set_minor_locator(otheryears)

for i in range(len(x)):
    #plt.plot_date(x[i],y[i],color='blue')
    plt.plot(x[i],y[i],c='#1f77b4')
#fig.autofmt_xdate()
plt.title('Benzene levels in Glasgow Kerbside from 2003-2011')
plt.xlabel('Time')
plt.ylabel('Micrograms per metre cubed')
plt.show()

