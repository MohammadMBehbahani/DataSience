from turtle import color
import matplotlib
import numpy as np
x = np.arange(0, 100)
y = x*2
z = x**2
import matplotlib.pyplot as plt
plt.show()

fig = plt.figure()

ax = fig.add_axex([0, 0, 1, 1])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('x')
ax.set_title('title')

fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, .5, .2])
ax1.plot(x, y)  
# ax1.plot(x, y, color='red')  
ax2.plot(x, y) 

fig = plt.figure()
ax =  fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([.2, .5, .4, .4])
ax.plot(x, z)
ax.set_xlabel('x')
ax.set_ylabel('z')

ax2.plot(x, y)
ax2.set_title('title')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])

fig, axes = plt.subplot(1, 2)

axes[0].plot(x,y, color='blue', lw=3, ls='--')
axes[1].plot(x,z, color='red', lw= 3)

fig, axes = plt.subplot(1, 2,figsize=(12, 2))

axes[0].plot(x,y, color='blue', lw=3, ls='--')
axes[1].plot(x,z, color='red', lw= 3)


