err_list = [0.0, 0.1301, 0.2427, 0.3285, 0.382, 0.4345, 0.4662, 0.4957, 0.5001, 0.5083, 0.5349, 0.5465, 0.6032, 0.674, 0.7544, 0.8666, 1.0]
err_lQEC = [0.0, 0.0504, 0.1517, 0.2531, 0.3287, 0.406, 0.4584, 0.4967, 0.5002, 0.5087, 0.5386, 0.5827, 0.6563, 0.7434, 0.855, 0.9484, 1.0]
params = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
err = {}
erq = {}
for num_party in [3]:
    err[num_party] = []
    erq[num_party] = []
    for param in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]:
        err[num_party].append(0.5*(1-(1-2*param)**num_party))
        erq[num_party].append(3*err[num_party][-1]**2*(1-err[num_party][-1])+err[num_party][-1]**3)

from matplotlib.pyplot import subplots, legend, show, savefig, rcParams
from matplotlib import rc

SIZE = 25
rc('font', size = SIZE)
rc('axes', titlesize=SIZE)
rcParams["figure.figsize"] = (13, 10)
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman'] + rcParams['font.serif']

fig, ax = subplots(1, 1)

ax.plot([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0], err[3], label = r'No encoding $e_1$, analytic', color = '#a00')
ax.plot([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0], erq[3], label = r'Repetition code $e_f$, analytic', ls = '--', color = '#00a')
ax.scatter([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0], err_list, label = r'No encoding $e_1$, simulation', marker = 'o', color = '#a00')
ax.scatter([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0], err_lQEC, label = r'Repetition code $e_f$, simulation', marker = '^', color = '#00a')

ax.set_xlabel(r'Channel error probability $p$')
ax.set_ylabel(r'Error on secret $e_1$ or $e_f$')

legend()

savefig("err_sim.png", format="png", bbox_inches="tight")

show()