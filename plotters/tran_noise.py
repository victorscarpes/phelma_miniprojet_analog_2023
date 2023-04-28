from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 2

with open("capture/data/tran_noise.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

T, Vout = np.split(result, 2, axis=1)
T = T.flatten()
Vout = Vout.flatten()

T_list = []
Vout_list = []

T_per = eng_inv("50 ns")
t0 = T[np.argmax(Vout[:1552])]

for i in range(len(T)):
    T[i] = T[i] - t0

for i in range(40):
    Vout_list.append(Vout[(T < eng_inv("50 ns")+i*T_per) & (eng_inv("-50 ns")+i*T_per < T)])
    T_list.append(T[(T < eng_inv("50 ns")+i*T_per) & (eng_inv("-50 ns")+i*T_per < T)])


for i in range(len(T_list)):
    T_list[i] = T_list[i] - i*T_per

fig, ax = plt.subplots()
fig.set_size_inches(fig_w, fig_h, forward=True)

for Ti, Vi in zip(T_list, Vout_list):
    ax.plot(Ti, Vi, color="C0", linewidth=0.1)

ax.set_xticks([eng_inv("-50 ns"), eng_inv("-25 ns"), eng_inv("0 ns"), eng_inv("25 ns"), eng_inv("50 ns")])
ax.xaxis.set_major_formatter(eng_formatter(unit='s', precision=2))
ax.yaxis.set_major_formatter(eng_formatter(unit='V', precision=4))
ax.set_xbound(eng_inv("-50 ns"), eng_inv("50 ns"))
ax.set_ylabel("$V_{out}$")
ax.set_xlabel("$\Delta t$")

plt.grid()
plt.tight_layout()
plt.savefig('plots/eye_diagram.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
