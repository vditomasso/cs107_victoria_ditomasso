#!/bin/usr/env python3

from Markov import Markov

weather_today = Markov()
weather_today.load_data()
print(weather_today.get_prob('sunny','cloudy'))
