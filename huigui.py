#!/usr/bin/env python

from scipy import stats
import numpy as np
import pylab

# x = np.array([1, 2, 5, 7, 10, 15])
# y = np.array([2, 6, 7, 9, 14, 19])
x = np.array([.5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4])
y = np.array([5.9, 4.9, 4.2, 3.7, 3.3, 2.95, 2.7, 2.45, 2.25, 2.1])

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
print slope, intercept

predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.plot(x, y, 'o')
pylab.plot(x, predict_y, 'k-')
pylab.show()