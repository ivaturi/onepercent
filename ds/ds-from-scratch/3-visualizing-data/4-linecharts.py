#! /usr/bin/python

from matplotlib import pyplot as plt

variance = [2**x for x in range(0, 9)]
bias_sq = [2**x for x in range(8, -1, -1)]
error = [x + y for x,y in zip(variance, bias_sq)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label="variance")
plt.plot(xs, bias_sq, 'r-.', label="bias")
plt.plot(xs, error, 'b:', label="error")

plt.legend(loc = 9)
plt.show()

# scatter plot
plt.scatter(variance, bias_sq)
plt.show()