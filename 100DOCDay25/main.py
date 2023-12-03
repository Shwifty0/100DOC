import pandas as pd


weather_data = pd.read_csv('weather_data.csv')

print(weather_data['day'].value_counts())