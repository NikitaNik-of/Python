import matplotlib.pyplot as plt
import numpy as np

fig10 = plt.figure(num=10, figsize=(5,5))
ax10 = fig10.add_subplot(1, 1, 1, projection='polar')
phi = np.linspace(0.0, 10*np.pi, 1000)
r = 5 - 5*np.cos(2.5*phi - 1)
ax10.plot(phi, r, linewidth=1.0)

plt.show()
