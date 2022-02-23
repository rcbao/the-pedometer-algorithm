# Name: Kathleen Nguyen, Robert Bao
# Email ID: cb5th
# Date: 2021-2-23
# File: main.py
# The signal analysis code for pedometer analysis

import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

file = open('data/acc_data.csv')  # read the csv file

csvreader = csv.reader(file)

header = []

header = next(csvreader)  # put the headers into an array

rows = []

for row in csvreader:  # read all the data into rows
    rows.append(row)

# print(rows)

# print(header)

time = []  # initialize the time and acceleration for each axes
ax = []
ay = []
az = []


def round_two_digits(input_num):
    return round(float(input_num), 2)


for row in rows:
    # appending all values into the array
    time.append(round_two_digits(row[0]))
    ax_data = round_two_digits(row[1])
    ax.append(ax_data)
    ay.append(row[2])
    az.append(row[3])

# print(time)
plt.plot(time, ax)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')

plt.gca().yaxis.set_major_locator(MaxNLocator(5))
plt.gca().xaxis.set_major_locator(MaxNLocator(10))

# locs, labels = plt.xticks()  # Get the current locations and labels
# plt.yticks(range(-1, 10))

plt.show()