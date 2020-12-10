#!/bin/usr/env python3

import numpy as np

class Markov:
    def __init__(self, day_zero_weather=None):
        self.data = np.empty(0)
        self.day_zero_weather = day_zero_weather
        
    def load_data(self, file_path = './weather.csv'):
        self.data = np.genfromtxt(file_path,delimiter=',')
    
    def get_prob(self, current_day_weather, next_day_weather):
        weather_dict = {'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
        try:
            return self.data[weather_dict[current_day_weather]][weather_dict[next_day_weather]]
        except KeyError:
            print('current_day_weather and next_day_weather must be one of the following strings:\n   sunny\n   cloudy\n   rainy\n   snowy\n   widny\n   hailing\nNot: {} and {}'.format(current_day_weather,next_day_weather))
            
    def __iter__(self):
        return MarkovIterator(self, self.day_zero_weather)
        
    def _simulate_weather_for_day(self, day):
        forecast = []
        for i in self:
            forecast.append(i)
        try:
            return forecast[day]
        except TypeError:
            print('day must be an int, not {}'.format(type(day)))

    def get_weather_for_day(self, day, trials):
        predictions = []
        for trial in range(trials):
            prediction = self._simulate_weather_for_day(day)
            predictions.append(prediction)
        return predictions

class MarkovIterator():

    global weather_dict
    weather_dict = {'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
    global index_dict
    index_dict = {v: k for k, v in weather_dict.items()}

    def __init__(self, Markov, day_zero_weather, n=14):
        self.n = n
        try:
            self.data = Markov.data
        except AttributeError:
            self.data = Markov.load_data()
            
        try:
            self.forecast = [day_zero_weather]
        except KeyError:
            print('day_zero_weather must be one of the following strings:\n   sunny\n   cloudy\n   rainy\n   snowy\n   widny\n   hailing\nNot: {} and {}'.format(day_zero_weather))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.forecast) == self.n+2:
            raise StopIteration
        else:
            current_day_weather = self.forecast[-1]
            ps = []
            for i in range(6):
                next_day_weather = index_dict[i]
                p = Markov.get_prob(self, current_day_weather, next_day_weather)
                ps.append(p)
            next_day_index = np.random.choice(6, 1, p=ps)
            next_day_weather = index_dict[next_day_index[0]]
            self.forecast.append(next_day_weather)
            return(current_day_weather)

