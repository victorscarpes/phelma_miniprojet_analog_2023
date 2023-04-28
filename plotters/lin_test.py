from matplotlib.ticker import PercentFormatter
from scipy.stats import linregress
from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np
print("\nlin_test")

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

with open("capture/data/linearite.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

Iin, Vout = np.split(result, 2, axis=1)
Iin = Iin.flatten()
Vout = Vout.flatten()

slope, intercept, r, p, se = linregress(Iin, Vout)

print(f"m = {round_eng(slope, unit='Ω', precision=6)}")
print(f"b = {round_eng(intercept, unit='V', precision=6)}")
print(f"r2 = {r**2}")

Vout_lin = slope*Iin + intercept

Vout_err = abs(Vout - Vout_lin)/(max(Vout_lin) - min(Vout_lin))

Verror_max = max(Vout_err)

print(f"Error = {round_fix(Verror_max*100, '%', 6)}")

fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax.plot(Iin, Vout, label="Données expérimentales")
ax.plot(Iin, Vout_lin, label="Linéarisation")
ax2.plot(Iin, Vout_err, label="Erreur en pourcentage", color="green")

ax.xaxis.set_major_formatter(eng_formatter(unit='A', precision=2))
ax.yaxis.set_major_formatter(eng_formatter(unit='V', precision=2))
ax2.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
ax2.xaxis.set_major_formatter(eng_formatter(unit='A', precision=2))


ax2.set_xlabel('$I_{in}$')
ax.set_ylabel('$V_{out}$')
ax2.set_ylabel('$\delta$')

ax2.set_xbound(min(Iin), max(Iin))

ax.legend(loc="best")
ax.grid()
ax2.grid()

plt.tight_layout()
plt.savefig('plots/lin_test.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
