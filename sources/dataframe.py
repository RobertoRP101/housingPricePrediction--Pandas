from dataset_retrieve import load_housing_data
from matplotlib import pyplot as plt 

housing = load_housing_data()
print(housing.head(5))
print(housing.shape)
print(housing.describe())
housing.hist(bins=50, figsize=(20,15))
plt.show()