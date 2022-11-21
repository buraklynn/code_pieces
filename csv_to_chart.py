import csv
import matplotlib.pyplot as plt
from datetime import datetime


file = 'weather.csv'
with open(file) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  
#  for index, column in enumerate(header_row):
#    print(index, column)

  dates, highs, lows = [], [], []
  for row in reader:
    try:
      high = int(row[6])
      low = int(row[7])
      date = datetime.strptime(row[5], '%Y%m%d')
    except ValueError:
      print("Datas couldn't upload to chart.")
    else:
      highs.append(high)
      lows.append(low)
      dates.append(date)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', label='High', alpha=0.7)
ax.plot(dates, lows, c='blue', label='Low', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='black', alpha=0.1)
plt.title('PETERSBURG Temperatures, January 2010', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.legend()
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
