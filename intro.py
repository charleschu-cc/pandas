import matplotlib.pyplot as plt
import pandas as pd

california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
california_housing_dataframe.hist('housing_median_age')
#plt.show()
