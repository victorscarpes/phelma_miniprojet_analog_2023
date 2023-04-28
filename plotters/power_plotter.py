from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 2

with open("capture/data/power.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

Iin, P = np.split(result, 2, axis=1)
Iin = Iin.flatten()
P = P.flatten()

fig, ax = plt.subplots()
fig.set_size_inches(fig_w, fig_h, forward=True)

ax.plot(Iin, P)
ax.xaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
ax.yaxis.set_major_formatter(eng_formatter(unit='W', precision=4))
ax.set_xbound(min(Iin), max(Iin))
ax.set_xlabel(r"$I_{in}$")

plt.grid()
plt.tight_layout()
plt.savefig('plots/power.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
