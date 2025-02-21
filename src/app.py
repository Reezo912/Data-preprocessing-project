import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# your code here

url = 'https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv'

df = pd.read_csv(url)

# Guardo el archivo
df.to_csv('./data/raw/AB_NYC_2019.csv', index = False )

df.drop(['name', 'host_name', 'reviews_per_month', 'last_review'], axis = 1, inplace = True)

print(df.info())

print(f'Duplicados: {df.duplicated().sum()}')

fig, axis = plt.subplots(2, 3, figsize = (10, 7))

sns.histplot(ax = axis[0, 0], data = df, x = "id").set_xlim(-0.1, 1.1)
sns.histplot(ax = axis[0, 1], data = df, x = "host_id").set(ylabel = None)
sns.histplot(ax = axis[0, 2], data = df, x = "neighbourhood").set(ylabel = None)
sns.histplot(ax = axis[1, 0], data = df, x = "latitude")
sns.histplot(ax = axis[1, 1], data = df, x = "price").set(ylabel = None)
sns.histplot(ax = axis[1, 2], data = df, x = "availavility_365").set(ylabel = None)