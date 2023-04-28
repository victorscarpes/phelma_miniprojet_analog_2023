from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np
print("\ngain_transimpedance")

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

with open("capture/data/gain_transimpedance.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

f, Rt, Xt = np.split(result, 3, axis=1)
f = f.flatten()
Rt = Rt.flatten()
Xt = Xt.flatten()

Zt = np.sqrt(Rt*Rt + Xt*Xt)
θ = np.unwrap(2 * np.arctan2(Xt, Rt))*90/np.pi

Z0 = Zt[0]
Zc = Z0/np.sqrt(2)

fc = f[(np.abs(Zt - Zc)).argmin()]

print(f"fc = {round_eng(fc, 'Hz', 6)}")
print(f"Z0 = {round_eng(Z0, 'Ω', 6)}")

fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax.plot(f, Zt, zorder=10)
ax.scatter([fc], [Zc], color="black", zorder=20)
ax.annotate(f"{round_eng(fc, 'Hz', 6)}\n{round_eng(Zc, 'Ω', 6)}",
            (fc, Zc),
            horizontalalignment='right',
            verticalalignment='top',
            textcoords='offset points',
            xytext=(-5, -5))
ax2.plot(f, θ)
ax.set_xscale("log")
ax.set_yscale("log")
ax2.xaxis.set_major_formatter(eng_formatter(unit='Hz', precision=1))
ax.yaxis.set_major_formatter(eng_formatter(unit='Ω', precision=1))
ax2.set_yticks([0, -90, -180, -270])
ax2.yaxis.set_major_formatter(fix_formatter(unit='°', precision=3, unit_space=False))
ax2.set_xbound(min(f), max(f))
ax.set_ylabel(r"$|Z_{T}|$")
ax2.set_ylabel(r"$\theta_{Z_{T}}$")

ax.grid()
ax2.grid()

plt.tight_layout()
plt.savefig('plots/gain_transimp.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
