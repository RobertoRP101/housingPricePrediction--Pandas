from dataset_retrieve import load_housing_data

housing = load_housing_data()
print(housing.head(5))
print(housing.shape)
print(housing.describe())