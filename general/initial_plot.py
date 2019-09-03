import sys as ss
ss.path.insert(1, '/Users/kevinfernandes/Documents/GitCodes_Projects/physics/optical')
import useful_Functions as usf

x = usf.np.linspace(0, 2*usf.np.pi, 100)
y = usf.np.sin(x)
z = usf.np.cos(x)
a = z**2
b = y**3

Fig = usf.plt.figure('Test fuctions')
ax1 = Fig.add_subplot(111)
ax1.set_xlabel('Angle (rad)')
ax1.set_ylabel('Amplitude (arb u.)')
ax1.plot(x, y, 'g')
ax1.plot(x, z, 'b')
ax1.plot(x, a, 'r')
ax1.plot(x, b, 'k')
ax1.grid(True)
ax1.autoscale(True)
usf.plt.show()
