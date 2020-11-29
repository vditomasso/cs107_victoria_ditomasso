#!/bin/usr/env python3

import numpy as np

class Markov:
    def __init__(self):
        self.data = np.empty(0)
        
    def load_data(self, file_path = './weather.csv'):
        self.data = np.genfromtxt(file_path,delimiter=',')
    
    def get_prob(self, current_day_weather, next_day_weather):
        weather_dict = {'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
        try:
            return self.data[weather_dict[current_day_weather]][weather_dict[next_day_weather]]
        except KeyError:
            print('current_day_weather and next_day_weather must be one of the following strings:\n   sunny\n   cloudy\n   rainy\n   snowy\n   widny\n   hailing\nNot: {} and {}'.format(current_day_weather,next_day_weather))

