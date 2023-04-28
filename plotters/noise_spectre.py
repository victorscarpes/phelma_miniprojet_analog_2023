from vspc_tools import *  # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np
print("\nnoise")

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

q = 1.602176634e-19

with open("capture/data/noise_spectre_input.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

f, spectre = np.split(result, 2, axis=1)
spectre = spectre.flatten()

with open("capture/data/integrated_input_noise.csv") as data:
    result = np.loadtxt(data, delimiter=",", skiprows=1)

f, rms = np.split(result, 2, axis=1)
f = f.flatten()
rms = rms.flatten()
Q = rms * eng_inv("1 ns")/q  # in equivalent electrons

Q_max = 1000
I_max = Q_max*q/eng_inv("1 ns")
f_max = f[(np.abs(Q - Q_max)).argmin()]
print(f"f_max = {round_eng(f_max, 'Hz', 6)}")

fig, (ax_spectre, ax_rms) = plt.subplots(nrows=2)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax_e = ax_rms.twinx()

ax_spectre.plot(f, spectre)
ax_spectre.set_xscale("log")
ax_spectre.set_yscale("log")
ax_spectre.xaxis.set_major_formatter(eng_formatter(unit='Hz', precision=1))
ax_spectre.yaxis.set_major_formatter(eng_formatter(unit='A/√Hz', precision=1))
ax_spectre.title.set_text("Spectre de bruit d'entrée")
ax_spectre.set_xbound(min(f), max(f))
ax_spectre.minorticks_off()
ax_spectre.grid()

ax_rms.plot(f, rms, zorder=10)
ax_rms.scatter([f_max], [I_max], color="black", zorder=20)
ax_rms.annotate(f"{round_eng(f_max, 'Hz', 6)}\n{round_eng(1000, 'e⁻', 1)}",
                (f_max, I_max),
                horizontalalignment='right',
                verticalalignment='bottom',
                textcoords='offset points',
                xytext=(-6, 1))
ax_rms.set_xscale("log")
ax_rms.set_yscale("log")
ax_rms.xaxis.set_major_formatter(eng_formatter(unit='Hz', precision=1))
ax_rms.yaxis.set_major_formatter(eng_formatter(unit='A', precision=1))
ax_rms.title.set_text("Bruit d'entrée intégré (RMS)")
ax_rms.set_xbound(min(f), max(f))
ax_rms.grid()

ax_e.set_yscale("log")
ax_e.set_xbound(min(f), max(f))
ax_e.set_yticks([I * eng_inv("1 ns")/q for I in ax_rms.get_yticks()])
ax_e.set_ybound(*[I * eng_inv("1 ns")/q for I in ax_rms.get_ybound()])
ax_e.yaxis.set_major_formatter(eng_formatter(unit='e⁻', precision=4))

plt.tight_layout()
plt.savefig('plots/input_noise.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
