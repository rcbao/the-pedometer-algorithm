# Name: Kathleen Nguyen, Robert Bao
# Email ID: cb5th
# Date: 2021-2-23
# File: main.py
# The signal analysis code for pedometer analysis

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

WINDOW_SIZE = 100

# OH Notes:
# The best way to get data from the phone sensor: put in the pants
# Hold the phone in hands is BAD
# - requires move hand FORWARD and BACKWARD
# - could be difficult
# Find local maxima is okay -- could have errors though


# round a number to 2 decimal points
def round_two_digits(input_num):
    return round(float(input_num), 2)


# get the rollowing average of a pandas series
def get_rolling_avg(input_series, window_size):
    windows = input_series.rolling(window_size)

    # Create a list of moving averages
    moving_averages = windows.mean().tolist()
    return moving_averages[window_size - 1:]


# thresholding function
def threshold_fn(x, threshold=3, step=2):
    res = pd.Series([0] * len(x), index=x.index)
    t = x.min() + threshold
    res.loc[x.gt(t)] = step
    return res


# input file: imported phyphox accelerometer -- without g
# also try: walk-10-step-2022-2-24-v2.csv !
filename = "data/walk-10-step-2022-2-24-v2.csv"
df = pd.read_csv(filename)
time = df["Time (s)"]
acc_x = df["Linear Acceleration y (m/s^2)"]

avg_time = get_rolling_avg(time, WINDOW_SIZE)
avg_acc_x = get_rolling_avg(acc_x, WINDOW_SIZE)

# find out if the data trend is increasing
series_avg_acc_x = pd.Series(avg_acc_x)
increasing_elements = series_avg_acc_x.diff().ge(0)

# shifted trend (local minima)
shifted = increasing_elements.ne(increasing_elements.shift())

# find the local max
local_max = shifted & (~increasing_elements)

# generate the step data by grouping sthe acceleration by the threshold
step = series_avg_acc_x.groupby(local_max.cumsum()).apply(threshold_fn)
step += series_avg_acc_x.min()

# difference from the previous row
step_change = step - step.shift(1)

# generate the final value count
value_count = step_change.value_counts()
positive_count = value_count[value_count.index > 0].iloc[0]

# plot the data using matplotlib
plt.plot(avg_time, avg_acc_x)
plt.plot(avg_time, step, drawstyle='steps')

# plotting settings
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.gca().yaxis.set_major_locator(MaxNLocator(5))
plt.gca().xaxis.set_major_locator(MaxNLocator(10))

plt.show()

print("=========================")
print("The Pedometer Algoirthm result")
print("Total step:", positive_count)
print("=========================")