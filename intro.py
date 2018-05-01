import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacremento'])
population = pd.Series([852469, 1015785, 485199])


california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
#print(california_housing_dataframe.describe())
#california_housing_dataframe.hist('housing_median_age')
#plt.show()

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
print(cities['City name'])
print(cities[0:2])

print(population / 1000)
print(np.log(population))
print(population.apply(lambda val: val > 1000000))

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))

print(cities)
