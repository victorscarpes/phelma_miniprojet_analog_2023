from vspc_tools import *   # Available at https://github.com/victorscarpes/vspc_tools
import matplotlib.pyplot as plt
import numpy as np
print("\nopen_loop")

plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams.update({'font.size': 14})
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
fig_w = 10
fig_h = 4

with open("capture/data/open_loop_gain_db.csv") as data:
    result_db = np.loadtxt(data, delimiter=",", skiprows=1)

f, gain = np.split(result_db, 2, axis=1)
gain = gain.flatten()

with open("capture/data/open_loop_phase.csv") as data:
    result_phase = np.loadtxt(data, delimiter=",", skiprows=1)

f, phase = np.split(result_phase, 2, axis=1)
f = f.flatten()
phase = phase.flatten()

A0 = gain[0]
print(f"A0 = {round_fix(A0, 'dB', 6)}")

index_0db = (np.abs(gain)).argmin()
f_0db = f[index_0db]
pm = 180 - (phase[0] - phase[index_0db])
print(f"\nf_0db = {round_eng(f_0db, 'Hz', 6)}")
print(f"pm = {round_fix(pm, '°', 6, unit_space=False)}")

index_180deg = (np.abs(phase[0] - phase - 180)).argmin()
f_180deg = f[index_180deg]
gm = -gain[index_180deg]
print(f"\nf_180deg = {round_eng(f_180deg, 'Hz', 6)}")
print(f"gm = {round_fix(gm, 'dB', 6)}")

fig, (ax_db, ax_phase) = plt.subplots(nrows=2, sharex=True)
fig.set_size_inches(fig_w, fig_h, forward=True)

ax_db.plot(f, gain, zorder=10)
ax_db.scatter([f_0db], [gain[index_0db]], color="black", zorder=20)
ax_db.annotate(f"{round_eng(f_180deg, 'Hz', 6)}\n{round_fix(0, 'dB', 1)}",
               (f_0db, 0),
               horizontalalignment='left',
               verticalalignment='bottom',
               textcoords='offset points',
               xytext=(5, 5))
ax_phase.plot(f, phase, zorder=30)
ax_phase.scatter([f_180deg], [phase[index_180deg]], color="black", zorder=40)
ax_phase.annotate(f"{round_eng(f_180deg, 'Hz', 6)}\n{round_fix(0, '°', 1, unit_space=False)}",
                  (f_180deg, 0),
                  horizontalalignment='left',
                  verticalalignment='bottom',
                  textcoords='offset points',
                  xytext=(5, 5))
ax_phase.set_xscale("log")
ax_phase.xaxis.set_major_formatter(eng_formatter(unit='Hz', precision=1))
ax_db.yaxis.set_major_formatter(fix_formatter(unit='dB', precision=2))
ax_phase.set_yticks([180, 90, 0, -90])
ax_phase.yaxis.set_major_formatter(fix_formatter(unit='°', precision=2, unit_space=False))
ax_phase.set_xbound(min(f), max(f))
ax_db.set_ylabel(r"$|A|$")
ax_phase.set_ylabel(r"$\theta_{A}$")

ax_db.grid()
ax_phase.grid()

plt.tight_layout()
plt.savefig('plots/open_loop.png', bbox_inches='tight')
if __name__ == "__main__":
    plt.show()
