import csv
from matplotlib import pyplot as plt

from datetime import datetime

date_one = datetime.strptime('2006-07-01', '%Y-%m-%d')
print(date_one)


filename = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\el_cajon_weather_2007.csv'

with open(filename) as fn:
    reader = csv.reader(fn)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # Get the max temperature from this file.

    dates, max_temps, low_temps = [], [], []

    for row in reader:
        recent_date = datetime.strptime(row[2], '%m/%d/%Y')
        try:

            max_temp = int(row[7])
            low_temp = int(row[8])
        except ValueError:
            print(f"Missing the data for that date")
        else:
            dates.append(recent_date)
            max_temps.append(max_temp)
            low_temps.append(low_temp)
    # print(max_temps)


#Plot the max temperatures.

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, max_temps,  c='red', alpha=0.5)
ax.plot(dates, low_temps, c='blue', alpha=0.5)
plt.fill_between(dates, max_temps, low_temps, color='blue', alpha=0.1)
#Form the plot

plt.title("Max and Low temperatures - 2006-2021 ", fontsize=25)

plt.xlabel('', fontsize=15)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.show()