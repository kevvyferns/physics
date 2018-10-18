import numpy as np
import matplotlib.pyplot as plt
import json as js

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)
a = z**2
b = y**3

Fig = plt.figure('Test fuctions')
ax1 = Fig.add_subplot(111)
ax1.set_xlabel('Angle (rad)')
ax1.set_ylabel('Amplitude (arb u.)')
ax1.plot(x, y, 'g')
ax1.plot(x, z, 'b')
ax1.plot(x, a, 'r')
ax1.plot(x, b, 'k')
ax1.grid(True)
ax1.autoscale(True)
plt.show()
