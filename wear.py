import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt

os.chdir(r'C:\Users\jegat\Desktop\py_work\work\project\to_plot')
files = os.listdir()
# files = ['5-1-H-w-Sheet2.csv']

for csv_file in files:
    with open(csv_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        times, wears = [], []
        for row in reader:
            try:
                if row[2].startswith('-'):
                    wear = float(row[2][1:-1])
                else:
                    wear = float(row[2][:-1])
                time = float(row[1][:-1])
            except:
                print(f"Missing data")
            else:
                times.append(time)
                wears.append(wear)

    # Plot the high and low temperatures.
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(times, wears, c="blue", alpha=0.9)
    # ax.plot(dates, lows, c="blue", alpha=0.7)
    # plt.fill_between(times, wears, lows, facecolor="blue", alpha=0.1)

    # # Format plot.
    # for 5 kg
    title = f"Wear plot, sample {csv_file[2]}, load - {csv_file[0]} kg"    
    # for 10, 15 kg
    # title = f"Wear plot, sample {csv_file[3]}, load - {csv_file[0:2]} kg"
    plt.title(title, fontsize=20)
    plt.xlabel("Time (s)", fontsize=16)
    plt.ylabel("Wear", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    # for 5 kg
    plt.savefig(f'sample {csv_file[2]} load {csv_file[0]} kg.png')
    # for 10, 15 kg
    # plt.savefig(f'sample {csv_file[3]} load {csv_file[0:2]} kg.png')
    # plt.show()
