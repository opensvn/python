#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

# x = np.arange(1, 1.5, 0.1)
# line, = plt.plot(x, -2.4* x + 5.34)
# lines = plt.plot(x, np.sin(x), x, np.cos(x))
# plt.setp(lines, color="r", linewidth=2.0)
# line.set_antialiased(False)
# for idx, color in enumerate("rgbyck"):
#     plt.subplot(320+idx+1, axisbg=color)
# plt.show()

'''x = 0.5 y = 5.9
x = 0.6 y = 4.9
x = 0.7 y = 4.2
x = 0.8 y = 3.7
x = 0.9 y = 3.3
x = 1 y = 2.95
x = 1.1 y = 2.7
x = 1.2 y = 2.45
x = 1.3 y = 2.25
x = 1.4 y = 2.1'''
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax.scatter(np.random.rand(20), np.random.rand(20)) # 返回值为CircleCollection对象
# ax.scatter([.5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4],
#     [5.9, 4.9, 4.2, 3.7, 3.3, 2.95, 2.7, 2.45, 2.25, 2.1])

# plt.show()