from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

with open("capture/data/tran_min_max_Iin/Iin_max_1m.csv") as data:
    result_1m = np.loadtxt(data, delimiter=",", skiprows=1)

T_max, Vout_1m = np.split(result_1m, 2, axis=1)
T_max = T_max.flatten()
Vout_1m = Vout_1m.flatten()

with open("capture/data/tran_min_max_Iin/Iin_min_1_9u.csv") as data:
    result_1_9u = np.loadtxt(data, delimiter=",", skiprows=1)

T_min, Vout_1_9u = np.split(result_1_9u, 2, axis=1)
T_min = T_min.flatten()
Vout_1_9u = Vout_1_9u.flatten()

fig, (ax_min, ax_max) = plt.subplots(nrows=2)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax_min.plot(T_min, Vout_1_9u)
ax_min.xaxis.set_major_formatter(eng_formatter(unit='s', precision=2))
ax_min.yaxis.set_major_formatter(eng_formatter(unit='V', precision=4))
ax_min.title.set_text("$I_{in} = 1,9\,\mu A$")
ax_min.set_xbound(eng_inv("100 ns"), eng_inv("350 ns"))
ax_min.set_ylabel("$V_{out}$")
# ax_min.set_xlabel("$t$")

ax_max.plot(T_max, Vout_1m)
ax_max.xaxis.set_major_formatter(eng_formatter(unit='s', precision=2))
ax_max.yaxis.set_major_formatter(eng_formatter(unit='V', precision=2))
ax_max.title.set_text("$I_{in} = 1\,mA$")
ax_max.set_xbound(eng_inv("100 ns"), eng_inv("350 ns"))
ax_max.set_ylabel("$V_{out}$")
# ax_max.set_xlabel("$t$")

ax_max.grid()
ax_min.grid()

plt.tight_layout()
plt.savefig('plots/tran.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
