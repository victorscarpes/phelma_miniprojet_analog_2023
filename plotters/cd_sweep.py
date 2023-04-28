from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

with open("capture/data/cd_sweep/iin_max_1m/cd_4_5p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_4_5p_max, Vout_4_5p_max = np.split(result, 2, axis=1)
T_4_5p_max = T_4_5p_max.flatten()
Vout_4_5p_max = Vout_4_5p_max.flatten()

with open("capture/data/cd_sweep/iin_max_1m/cd_9p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_9p_max, Vout_9p_max = np.split(result, 2, axis=1)
T_9p_max = T_9p_max.flatten()
Vout_9p_max = Vout_9p_max.flatten()

with open("capture/data/cd_sweep/iin_max_1m/cd_18p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_18p_max, Vout_18p_max = np.split(result, 2, axis=1)
T_18p_max = T_18p_max.flatten()
Vout_18p_max = Vout_18p_max.flatten()


# ----------------------

with open("capture/data/cd_sweep/iin_min_1_9u/cd_4_5p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_4_5p_min, Vout_4_5p_min = np.split(result, 2, axis=1)
T_4_5p_min = T_4_5p_min.flatten()
Vout_4_5p_min = Vout_4_5p_min.flatten()

with open("capture/data/cd_sweep/iin_min_1_9u/cd_9p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_9p_min, Vout_9p_min = np.split(result, 2, axis=1)
T_9p_min = T_9p_min.flatten()
Vout_9p_min = Vout_9p_min.flatten()

with open("capture/data/cd_sweep/iin_min_1_9u/cd_18p.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T_18p_min, Vout_18p_min = np.split(result, 2, axis=1)
T_18p_min = T_18p_min.flatten()
Vout_18p_min = Vout_18p_min.flatten()

fig, (ax_min, ax_max) = plt.subplots(nrows=2)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax_min.plot(T_4_5p_min, Vout_4_5p_min, label=r"$C_{d} = 4.5\,pF$", linewidth=1.3)
ax_min.plot(T_9p_min, Vout_9p_min, label=r"$C_{d} = 9\,pF$", linewidth=1.3)
ax_min.plot(T_18p_min, Vout_18p_min, label=r"$C_{d} = 18\,pF$", linewidth=1.3)
ax_min.xaxis.set_major_formatter(eng_formatter(unit='s', precision=2))
ax_min.yaxis.set_major_formatter(eng_formatter(unit='V', precision=4))
ax_min.title.set_text("$I_{in} = 1,9\,\mu A$")
ax_min.set_xbound(eng_inv("0 ns"), eng_inv("650 ns"))
ax_min.set_ylabel("$V_{out}$")
ax_min.legend(loc='upper left')
ax_min.grid()

ax_max.plot(T_4_5p_max, Vout_4_5p_max, label=r"$C_{d} = 4.5\,pF$", linewidth=1.3)
ax_max.plot(T_9p_max, Vout_9p_max, label=r"$C_{d} = 9\,pF$", linewidth=1.3)
ax_max.plot(T_18p_max, Vout_18p_max, label=r"$C_{d} = 18\,pF$", linewidth=1.3)
ax_max.xaxis.set_major_formatter(eng_formatter(unit='s', precision=2))
ax_max.yaxis.set_major_formatter(eng_formatter(unit='V', precision=1))
ax_max.title.set_text("$I_{in} = 1\,mA$")
ax_max.set_xbound(eng_inv("0 ns"), eng_inv("650 ns"))
ax_max.set_ylabel("$V_{out}$")
ax_max.legend(loc='upper left')
ax_max.grid()

plt.tight_layout()
plt.savefig('plots/tran_cd_sweep.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
