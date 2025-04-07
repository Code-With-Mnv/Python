# toyota_visualizations.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Toyota.csv")

plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Price'], alpha=0.6, color='green')
plt.title('Car Price vs Age')
plt.xlabel('Age (Years)')
plt.ylabel('Price')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['KM'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(6, 4))
fuel_counts = df['FuelType'].value_counts()
fuel_counts.plot(kind='bar', color='orange')
plt.title('Number of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(6, 6))
fuel_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Cars by Fuel Type')
plt.ylabel('')
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(x='FuelType', y='Price', data=df)
plt.title('Car Price Distribution by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.show()
