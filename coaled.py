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
print(tips.head())