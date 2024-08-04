import sqlite3
import pandas as pd

# Create a connection to a new SQLite database
conn = sqlite3.connect('weather_data.db')

# Load dataset and write to SQL
df = pd.read_csv('1. Weather Data.csv')
print("DataFrame columns:", df.columns)  # This line prints the column names
df.to_sql('weather', conn, if_exists='replace', index=False)

# SQL queries
query1 = "SELECT * FROM weather WHERE Weather = 'Clear';"
clear_weather_records_sql = pd.read_sql(query1, conn)
print(clear_weather_records_sql)

query2 = "SELECT COUNT(*) FROM weather WHERE `Wind Speed_km/h` = 4;"
wind_speed_4_count_sql = pd.read_sql(query2, conn)
print(f"Number of times wind speed was exactly 4 km/h: {wind_speed_4_count_sql.iloc[0, 0]}")

query3 = "SELECT COUNT(*) FROM weather WHERE `Wind Speed_km/h` > 24 AND Visibility_km = 25;"
filtered_records_count_sql = pd.read_sql(query3, conn)
print(f"Number of records where wind speed > 24 km/h and visibility = 25 km: {filtered_records_count_sql.iloc[0, 0]}")

query4 = "SELECT Weather, AVG(Visibility_km) AS Mean_Visibility FROM weather GROUP BY Weather;"
mean_visibility_by_weather_sql = pd.read_sql(query4, conn)
print("Mean visibility for each weather condition:\n", mean_visibility_by_weather_sql)
