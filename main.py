# Name: Kathleen Nguyen, Robert Bao
# Email ID: cb5th
# Date: 2021-2-23
# File: main.py
# The signal analysis code for pedometer analysis

print("HELLO cs 4501!")

import csv
import matplotlib.pyplot as plt

file = open('data/acc_data.csv') # read the csv file

csvreader = csv.reader(file)

header = []

header = next(csvreader) # put the headers into an array

rows = []

for row in csvreader: # read all the data into rows
    rows.append(row)

# print(rows)

# print(header)

time = [] # initialize the time and acceleration for each axes
ax = []
ay = []
az = []

for row in rows:
    time.append(row[0]) # appending all values into the array
    ax.append(row[1])
    ay.append(row[2])
    az.append(row[3])

print(time)

plt.plot(time,ax)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
locs, labels = plt.xticks()  # Get the current locations and labels

plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

plt.show()