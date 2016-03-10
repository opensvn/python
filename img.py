#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# x = np.arange(0,6)
# y = x * x

# x = np.array([.5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4])
# y = np.array([5.9, 4.9, 4.2, 3.7, 3.3, 2.95, 2.7, 2.45, 2.25, 2.1])

# x = np.array([.6, .7, .8, .9])#, 1.0, 1.1, 1.2])
# y = np.array([-9.5, -8.5, -7.5, -6.5])#, -7.5, -7, -6.5])

# x = np.array([1.0, 1.1, 1.2])
# y = np.array([-7.5, -7, -6.5])

x = np.array([.6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
y = np.array([-19, -16, -14, -12.5, -11.5, -10, -9.5, -9, -8, -7.5])

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
print slope, intercept

predict_y = intercept + slope * x
formula = 'y = %f + %f * x' % (intercept, slope)
 
plt.plot(x, y, marker='o')
for xy in zip(x,y):
    plt.annotate("(%s, %s)" % xy, xy=xy, xytext=(-20,10), textcoords = 'offset points')
plt.plot(x, predict_y, 'k-', label=r"$"+formula+"$",color="red",linewidth=2)
# plt.xlabel("x")
# plt.ylabel("y")
plt.show()

# import matplotlib.pyplot as plt
# from numpy import arange

# x = arange(1,1000,1)
# r = -2
# c = 5
# y = [5*(a**r) for a in x]

 

# fig = plt.figure()

# ax = fig.add_subplot(111)
# ax.loglog(x,y,label = r"$y = \frac{1}{2\sigma_1^2}, c=5,\sigma_1=-2$")
# ax.legend()
# ax.set_xlabel(r"x")
# ax.set_ylabel(r"y")

# plt.show()