# Questions to be answered : 
# Which hour has the highest frequency of crimes? 
# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? 
# Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+).
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
crimes = pd.read_csv('crimes.csv', dtype = {'TIME OCC': str}) 

crimes['DATE OCC'] = pd.to_datetime(crimes['DATE OCC'])
crimes['Date Rptd'] = pd.to_datetime(crimes['Date Rptd'])


crimes.isna().sum()
# As there is no misssing value in Crm Cd Desc, all records refer a crime.

# Which hour has the highest frequency of crimes? 
crimes['HOUR OCC'] = crimes['TIME OCC'].str[:2].astype(int)
peak_crime_hour = crimes['HOUR OCC'].value_counts(normalize= True).idxmax(0)
print(peak_crime_hour, 'has the highest frequency of crimes.')
sns.countplot(data = crimes, x= 'HOUR OCC')
plt.xlabel('Hour crime occured')
plt.ylabel('Count of crimes')
plt.clf()

# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? 
night_crime = crimes[(crimes['HOUR OCC'] >= 22) | (crimes['HOUR OCC'] < 4)]
peak_night_crime_location = night_crime['AREA NAME'].value_counts(normalize= True).idxmax(0)
print(peak_night_crime_location, 'has the largest frequency of night crimes.')
sns.countplot(data = night_crime, x= 'AREA NAME')
plt.xlabel('Area crime occured')
plt.xticks(rotation = 45)
plt.ylabel('Count of crimes')
plt.clf()

# Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+).
crimes['Vict Age'].describe()
# It seems there are people whose age is below zero in our data.
age_to_remove = crimes[crimes['Vict Age'] < 0].index
crimes.drop(age_to_remove, inplace = True)

age_group = ['0-17','18-25','26-34','35-44','45-54','55-64','65+']
bins = [0,17,25,34,44,54,64,100]
crimes['VICT_AGE_GROUP'] = pd.cut(crimes['Vict Age'],labels= age_group, bins= bins)
victim_ages = crimes['VICT_AGE_GROUP'].value_counts()
sns.countplot(data = crimes, x='VICT_AGE_GROUP', hue='Vict Sex')
plt.xlabel('Age group of victim')
plt.ylabel('Count of crimes')
plt.show()