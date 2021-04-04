#! /usr/bin/python

# This is an example of using a bar chart to plot 
# a distribution of values, as a histogram

from collections import Counter
from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 75, 73, 77, 10, 23, 34, 56, 74, 65]

# Include 100 in the 90s
hist = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in hist.keys()],   # move the bars a lttle to the right 
        hist.values(),
        10)                             # bar width


plt.axis([-5, 105, 0, 6])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("Number of students")
plt.title("Grade distribution")
plt.show()