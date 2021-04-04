#! /usr/bin/python

from matplotlib import pyplot as plt

# set up data
movies = ["Annie hall", "Ben-hur", "Casablanca", "Gandhi", "West side story"]
num_oscars = [5, 11, 3, 8, 10]

# plot...
plt.bar(range(len(movies)), num_oscars)
plt.title("Some movies")
plt.ylabel("Number of academy awards")
plt.xticks(range(len(movies)), movies)
plt.show()