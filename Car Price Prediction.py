import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

carDataSet = pd.read_csv("quikr_car.csv") 
print(carDataSet.head(5))

print(carDataSet.shape)
print(carDataSet.info)

backUp = carDataSet.copy()
print(backUp)

carDataSet = carDataSet[carDataSet['year'].str.isnumeric()]
carDataSet['year'] = carDataSet['year'].astype(int)
carDataSet = carDataSet[carDataSet['Price'] != 'Ask For Price']
carDataSet['Price'] = carDataSet['Price'].str.replace(',', '').astype(int)
carDataSet['kms_driven'] = carDataSet['kms_driven'].str.split().str.get(0).str.replace(',', '')
carDataSet = carDataSet[carDataSet['kms_driven'].str.isnumeric()]
carDataSet['kms_driven'] = carDataSet['kms_driven'].astype(int)
carDataSet = carDataSet[~carDataSet['fuel_type'].isna()]
print(carDataSet.shape)

carDataSet['name']=carDataSet['name'].str.split().str.slice(start=0,stop=3).str.join(' ')
carDataSet=carDataSet.reset_index(drop=True)
print(carDataSet)

carDataSet.to_csv('Cleaned_Car_data.csv')
print(carDataSet.info)
carDataSet.describe(include='all')
carDataSet=carDataSet[carDataSet['Price']<9000000]
print(carDataSet['company'].unique())

plt.subplots(figsize=(15,7))
ax=sns.boxplot(x='company',y='Price',data=carDataSet)
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
plt.show()

plt.subplots(figsize=(20,10))
ax=sns.swarmplot(x='year',y='Price',data=carDataSet)
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
plt.show()
sns.relplot(x='kms_driven',y='Price',data=carDataSet,height=7,aspect=1.5)
