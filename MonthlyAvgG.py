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

datasets = [db03,db04,db05,db06,db07,db08,db09,db10]

x=[]
y=[]

# Create empty lists
Avg03,Avg04,Avg05,Avg06,Avg07,Avg08,Avg09,Avg10 = ([] for i in range(8))

# Create array of lists of each of the years
MonthlyAverages = [Avg03,Avg04,Avg05,Avg06,Avg07,Avg08,Avg09,Avg10]

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
    for j in range(len(NewVOC)):
        NewVOC[j] = float(NewVOC[j])   

    # Set the indices as the date
    NewVOC.index = NewDate
    NewVOC = pd.to_numeric(NewVOC)

    # Calculate the monthly averages for each year
    MonthAvg = NewVOC.resample('M').mean()

    # Add the monthly averages to the corresponding year
    MonthlyAverages[i].append(MonthAvg)
    
# Calculate total monthly average for each month over the years 1998-2019
y=[]
for m in range(12):
    y.append(np.nanmean(np.dstack((MonthlyAverages[0][0][m],MonthlyAverages[1][0][m]\
                                ,MonthlyAverages[2][0][m],MonthlyAverages[3][0][m]\
                                ,MonthlyAverages[4][0][m],MonthlyAverages[5][0][m]\
                                ,MonthlyAverages[6][0][m],MonthlyAverages[7][0][m])),2))         

    # Convert the averages to floats
    y[m]=np.float(y[m])

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plot a bar chart
fig, ax = plt.subplots(figsize=(10.5,6))
plt.bar(x,y,color='#1f77b4')
plt.title('Average benzene levels per month in Glasgow Kerbside from 2003-2011')
plt.xlabel('Months')
plt.ylabel('Micrograms per metre cubed')
plt.show()

