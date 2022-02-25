# Name: Kathleen Nguyen, Robert Bao
# Email ID: cb5th
# Date: 2021-2-23
# File: main.py
# The signal analysis code for pedometer analysis

import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

WINDOW_SIZE = 100

# best way to get data from the phone sensor:
# - MOVE THE ARM == BAD
#   - requires move hand FORWARD and BACKWARD
# - Better: put in the pants
# best case:
# - 1 valley + 1 peak
# - constant amplitude

# Find local maxima is okay
# could have errors though


# round a number to 2 decimal points
def round_two_digits(input_num):
    return round(float(input_num), 2)


# get the rollowing average of a pandas series
def get_rolling_avg(input_series, window_size):
    windows = input_series.rolling(window_size)

    # Create a list of moving averages
    moving_averages = windows.mean().tolist()
    return moving_averages[window_size - 1:]


filename = "data/walk-10-step-2022-2-24-v2.csv"
df = pd.read_csv(filename)
time = df["Time (s)"]
acc_x = df["Acceleration y (m/s^2)"]
print(type(acc_x))

avg_time = get_rolling_avg(time, WINDOW_SIZE)
avg_acc_x = get_rolling_avg(acc_x, WINDOW_SIZE)

# if the data trend is increasing
series_avg_acc_x = pd.Series(avg_acc_x)
incr = series_avg_acc_x.diff().ge(0)

# shifted trend (local minima)
shifted = incr.ne(incr.shift())

# local max
local_max = shifted & (~incr)


# thresholding function
def thresh(x, threshold=3, step=2):
    ret = pd.Series([0] * len(x), index=x.index)
    t = x.min() + threshold
    ret.loc[x.gt(t)] = step
    return ret


signal = series_avg_acc_x.groupby(local_max.cumsum()).apply(thresh)
signal += series_avg_acc_x.min()
# print(signal[200:])

plt.plot(avg_time, avg_acc_x)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')

# difference from the previous row
signal_change = signal - signal.shift(1)

print(signal_change[:200])
value_count = signal_change.value_counts()
print(value_count)
print(type(value_count))

plt.plot(avg_time, signal, drawstyle='steps')

plt.gca().yaxis.set_major_locator(MaxNLocator(5))
plt.gca().xaxis.set_major_locator(MaxNLocator(10))

plt.show()