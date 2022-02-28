# Name: Kathleen Nguyen, Robert Bao
# Email ID: kn7wz, cb5th
# Date: 2021-2-28
# File: plot_raw_data.py
# Plot raw data for pedometer analysis
# To run this script, execute this: `python plot_raw_data.py`

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

WINDOW_SIZE = 1


# get the rollowing average of a pandas series
def get_rolling_avg(input_series, window_size):
    windows = input_series.rolling(window_size)

    # Create a list of moving averages
    moving_averages = windows.mean().tolist()
    return moving_averages[window_size - 1:]


# input file: imported phyphox accelerometer -- without g
# also try: walk-10-step-2022-2-24-v2.csv !
# Note: This will not work with data with g. (The value range is different)
filename = "data/walk-10-step-2022-2-24-v1.csv"
df = pd.read_csv(filename)
time = df["Time (s)"]
acc = df["Linear Acceleration y (m/s^2)"]

avg_time = get_rolling_avg(time, WINDOW_SIZE)
avg_acc = get_rolling_avg(acc, WINDOW_SIZE)

# plot the data using matplotlib
fig, ax = plt.subplots()

ax.plot(avg_time, avg_acc, label="The Average Acceleration")
ax.legend()

# plotting settings
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration $(m/s^2)$')
ax.yaxis.set_major_locator(MaxNLocator(5))
ax.xaxis.set_major_locator(MaxNLocator(10))

title_style = {
    'verticalalignment': 'baseline',
    'horizontalalignment': "center"
}
text = "Plot for Raw Data"
plt.style.use('seaborn')
plt.title(label=text, fontdict=title_style)
plt.show()
