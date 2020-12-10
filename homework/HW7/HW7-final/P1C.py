#!/bin/usr/env python3

import numpy as np
from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

weather_types = ['sunny','cloudy','rainy','snowy','windy','hailing']

forecasts = []

for key, value in city_weather.items():
    weather_today = Markov(value)
    weather_today.load_data()
    city_forecast = weather_today.get_weather_for_day(7,100)
    forecasts.append(np.array(city_forecast))
    
city_forecast_dicts = []
    
for key, city_forecast in zip(city_weather.keys(), forecasts):
    city_forecast_dict = {}
#    weather_type_occurances = []
    for weather_type in weather_types:
        occurance = np.count_nonzero(city_forecast == weather_type)
#        weather_type_occurances.append(occurances)
        city_forecast_dict.update({weather_type:occurance})
    city_forecast_dicts.append(city_forecast_dict)
    print(key, ':', city_forecast_dict)

print('\nMost likely weather in seven days')
print('----------------------------------')

for key, city_forecast_dict in zip(city_weather.keys(), city_forecast_dicts):
    Keymax = max(city_forecast_dict, key=city_forecast_dict.get)
    print('{}: {}'.format(key,Keymax))
