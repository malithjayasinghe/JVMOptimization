import subprocess
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import pylab as plt
import statsmodels.api as sm
from statsmodels.nonparametric.kde import kernel_switch

#from pyqt_fit import kde
execution_times = []
for x in range(100):
        p = subprocess.Popen("/Users/malithjayasinghe/JVMOptimization/jvm_optimization/run_integration", shell=True, stdout=subprocess.PIPE)
        for line in p.stdout:
                print(line)
        p.wait()
        f = open("response_time.txt", "r")
        run_time = float(f.readline())
        execution_times.append(run_time)
        print("run time " + str(run_time) + "X = "+ str(int(x)))


kde = sm.nonparametric.KDEUnivariate(execution_times)
kde.fit() # Estimate the densities
h= plt.dens(execution_times, bins=30, normed=True, color=(0,.5,0,1), label='Histogram')
#plt.plot(execution_times, ys, 'r--', linewidth=2, label='$\mathcal{N}(0,1)$')
plt.plot(kde.support, kde.density, lw=3, label='KDE from samples', zorder=10)
plt.xlim(40,60)
plt.xlabel('Execution Time')
plt.show()

