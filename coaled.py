import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('http://analityk.edu.pl/wp-content/uploads/2020/01/World_Bank_CO2_cleaned.xlsx')
#print(df.head())

df = df[~df['CO2 (kt)'].isnull() & ~df['CO2 Per Capita (metric tons)'].isnull() & (df['Year'] > 1980)]
#print(df.head())

df_pl = df[df['Country Name'] == 'Poland']
#print(df_pl.head())

tips = sns.load_dataset('tips')
#print(tips.head())


sns.relplot(data = df[(df['Country Name'] == 'Poland') | (df['Country Name'] == 'France')],
            x = 'Year',
            y = 'CO2 (kt)',
            aspect = 2.5,
            kind='line', #(1)scatter
            hue = 'Country Name') #(1) col='Country Name'
#plt.show()

sns.relplot(x='total_bill',
            y='tip',
            aspect=2.5,
            data=tips,
            size='size',
            hue='smoker',
            kind='scatter');
#plt.show()

sns.catplot(x='Region',
            y='CO2 Per Capita (metric tons)',
            data=df[df['Year'] == 2010],
            aspect=2.5)
#plt.show()

tips = sns.load_dataset('tips')
sns.catplot(x='day',
            y='tip',
            aspect=2.5,
            data=tips,
            kind='box',
            hue='sex')
#plt.show()

# sns.implot(data=df[((df['Country Name'] == 'Poland') | (df['Country Name'] == 'France'))],

tips = sns.load_dataset('tips')
sns.distplot(tips['tip'],bins=10)
#plt.show()

sns.distplot(tips[tips['day'] == 'Sun']['tip'], bins=10, kde_kws={'Label' : 'Sunday'})
sns.distplot(tips[tips['day'] == 'Fri']['tip'], bins=10, kde_kws={'Label' : 'Friday'})
plt.show()