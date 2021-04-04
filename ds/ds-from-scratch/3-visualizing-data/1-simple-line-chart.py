#! /usr/bin/python
from matplotlib import pyplot as plt

# set up data
years = [1950 + i*10 for i in range(7)]
print(years)
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# draw a line chart with years on x-axis and gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title to the plot
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions USD")
plt.show()