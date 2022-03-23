import matplotlib.pyplot as plt
import numpy as np

fig05 = plt.figure(num=4, figsize=(10, 2))

axs05 = [fig05.add_subplot(1, 3, i) for i in range(1,4)]

x = np.linspace(-2,2,100)
funcs = [x, x**2, x**3]

y_min = np.min(funcs)
y_max = np.max(funcs)
for (f, ax) in zip(funcs, axs05):
    ax.plot(x, f)
    ax.set_ylim(bottom=y_min, top=y_max)
    ax.grid(True)
for ax in axs05[1:]:
    ax.set_yticklabels([])

fig05.subplots_adjust(wspace=0)

plt.show()