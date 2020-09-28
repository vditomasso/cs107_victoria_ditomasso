#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import datetime

def clock_hand(r):
    '''Outer function for finding the position of a clock hand
    Input:
    r: float
        Length of the clock hand
        
    Returns:
    find_hand_pos: function'''
    
    def find_hand_pos(theta):
        '''Closure for finding the position of a clock hand
        Input:
        theta: float
            The angle of the clock hand at the desired time, in degrees
        
        Returns:
        x: float
            x coordinate of non-origin end of the clock hand
        y: float
            y coordinate of non-origin end of the clock hand'''
        
        theta_rad = (np.pi/180) * theta
        x = r * np.cos(theta_rad)
        y = r * np.sin(theta_rad)
        
        return(x,y)

    return(find_hand_pos)

# Demo
currentDT = datetime.datetime.now()
hour = currentDT.hour
if hour>=12:
    hour = hour-12
minute = currentDT.minute
second = currentDT.second

#print(hour, minute, second)

# Calculate the theta in degrees for each hand
theta_hour = 90-(30*hour)-(minute/2)
theta_minute = 90-(6*minute)
theta_second = 90-(6*second)

# Specify the length of hour, minute and second hands
r_hour = 1
r_minute = 2
r_second = 3

# Create the function for finding the position of each hand
hour_hand = clock_hand(r_hour)
minute_hand = clock_hand(r_minute)
second_hand = clock_hand(r_second)

# Find the x, y position for each of the hands
x_hour, y_hour = hour_hand(theta_hour)
x_minute, y_minute = minute_hand(theta_minute)
x_second, y_second = second_hand(theta_second)

# Plot the clock
fig, ax = plt.figure(figsize=[6,6]), plt.gca()
ax.plot([0,x_hour],[0,y_hour])
ax.plot([0,x_minute],[0,y_minute])
ax.plot([0,x_second],[0,y_second])
circle = plt.Circle((0,0), 3.2, edgecolor='black', fill=False)
ax.add_patch(circle)
plt.show()
