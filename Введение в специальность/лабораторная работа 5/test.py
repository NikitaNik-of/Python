import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-4*np.pi, 4*np.pi, 400)
x = np.sin(t) + np.cos(t) + np.cos(2*t)
y = np.cos(2*t) + np.sin(np.cos(t))

fig04 = plt.figure(10)
ax04 = fig04.add_subplot(1, 1, 1)
ax04.grid()
label_01 = r'$\sin({t}) + \cos({t}) + \cos({2t})$'
label_02 = r'$\cos{(2t)} + \sin{[\cos{(t)}]}$'
ax04.plot(t, x, linewidth=1.0, linestyle='-', marker='None', label=label_01)
ax04.plot(t, y, linewidth=0.5, linestyle='-', marker='.', markevery=4, markersize=3, label=label_02)
ax04.legend(ncol=2, title='Легенда', framealpha=0.7, fontsize=12)

xticks = np.linspace(-4*np.pi, 4*np.pi, 9)
xtickslabels = []
for xtick in xticks:
    i = int(xtick/np.pi)
    if i == 1:
        xtickslabels.append(r'$\pi$')
    elif i == -1:
        xtickslabels.append(r'-$\pi$')
    elif i == 0:
        xtickslabels.append(r'0')
    else:
        xtickslabels.append(r'{0}$\pi$'.format(i))
ax04.set_xticks(xticks)
ax04.set_xticklabels(xtickslabels)

plt.show()