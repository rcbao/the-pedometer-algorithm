# Name: Kathleen Nguyen, Robert Bao
# Email ID: cb5th
# Date: 2021-2-23
# File: main.py
# The signal analysis code for pedometer analysis

import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

WINDOW_SIZE = 50


def round_two_digits(input_num):
    return round(float(input_num), 2)


def get_rolling_avg(input_series, window_size):
    windows = input_series.rolling(window_size)

    # Create a list of moving averages
    moving_averages = windows.mean().tolist()
    return moving_averages[window_size - 1:]


df = pd.read_csv('data/acc_data.csv')
time = df["Time (s)"]
acc_x = df["Acceleration x (m/s^2)"]
print(type(acc_x))

avg_time = get_rolling_avg(time, WINDOW_SIZE)
avg_acc_x = get_rolling_avg(acc_x, WINDOW_SIZE)

# print(time)
plt.plot(avg_time, avg_acc_x)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')

plt.gca().yaxis.set_major_locator(MaxNLocator(5))
plt.gca().xaxis.set_major_locator(MaxNLocator(10))

plt.show()