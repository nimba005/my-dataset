
import pandas as pd
# Load dataset
df = pd.read_csv('dataset/your-dataset.csv')

# Find all records where the weather was exactly clear
clear_weather_records = df[df['Weather'] == 'Clear']
print(clear_weather_records)

# Find the number of times the wind speed was exactly 4 km/hr
wind_speed_4_count = df[df['Wind Speed'] == 4].shape[0]
print(f"Number of times wind speed was exactly 4 km/hr: {wind_speed_4_count}")

# Check if there are any NULL values present in the dataset
null_values = df.isnull().sum()
print("NULL values in each column:\n", null_values)

# Rename the column "Weather" to "Weather_Condition."
df.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)
print(df.head())

# Mean visibility of the dataset
mean_visibility = df['Visibility'].mean()
print(f"Mean visibility of the dataset: {mean_visibility}")

# Number of records where wind speed is greater than 24 km/hr and visibility is equal to 25 km
filtered_records = df[(df['Wind Speed'] > 24) & (df['Visibility'] == 25)]
num_filtered_records = filtered_records.shape[0]
print(f"Number of records where wind speed > 24 km/hr and visibility = 25 km: {num_filtered_records}")

# Mean value of each column for each weather condition
mean_values_by_weather = df.groupby('Weather_Condition').mean()
print("Mean values for each weather condition:\n", mean_values_by_weather)

# Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40
filtered_instances = df[(df['Weather_Condition'] == 'Clear') & (df['Relative Humidity'] > 50) |
                         (df['Visibility'] > 40)]
print(filtered_instances)

# Number of weather conditions that include snow
snow_conditions_count = df['Weather_Condition'].str.contains('Snow').sum()
print(f"Number of weather conditions that include snow: {snow_conditions_count}")
