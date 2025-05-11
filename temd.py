damp_err_list = [0.0, 0.0216, 0.0413, 0.0635, 0.0883, 0.1053, 0.1976, 0.2588, 0.3291, 0.3773, 0.4297, 0.475, 0.4997]
damp_err_lQEC = [0.0, 0.0009, 0.0056, 0.0124, 0.0203, 0.0307, 0.1001, 0.172, 0.2611, 0.3316, 0.3912, 0.4638, 0.5044]

from matplotlib.pyplot import subplots, legend, show, savefig, rcParams
from matplotlib import rc

SIZE = 12
rc('font', size = SIZE)
rc('axes', titlesize=SIZE)
# rcParams["figure.figsize"] = (, 10)
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman'] + rcParams['font.serif']

fig, ax = subplots(1, 1)

ax.plot([0.0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0], damp_err_list, label = r'No encoding $e_1$', color = '#a00')
ax.plot([0.0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0], damp_err_lQEC, label = r'Repetition code $e_f$', color = '#00a', ls = "--")

ax.set_xlabel(r'Channel damping strength $\gamma$')
ax.set_ylabel(r'Error on secret $e_1$ or $e_f$')

ax.legend()

savefig("err_amp.png", format="png", bbox_inches="tight")

show()