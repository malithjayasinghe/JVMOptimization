import subprocess
from matplotlib import pylab as plt
import statsmodels.api as sm
from scipy.stats import shapiro
from scipy.stats import norm
import numpy as np

execution_times = []
for x in range(50):
        p = subprocess.Popen("/Users/malithjayasinghe/JVMOptimization/jvm_optimization/run_integration", shell=True, stdout=subprocess.PIPE)
        for line in p.stdout:
                print(line)
        p.wait()
        f = open("response_time.txt", "r")
        run_time = float(f.readline())
        execution_times.append(run_time)
        print("run time " + str(run_time) + "X = "+ str(int(x)))

stat, p = shapiro(execution_times)

alpha = 0.05
print(p)
mu, std = norm.fit(execution_times)

if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
else:
        print('Sample does not look Gaussian (reject H0)')


kde = sm.nonparametric.KDEUnivariate(execution_times)
kde.fit() # Estimate the densities
h= plt.hist(execution_times, 'auto', normed=True, color=(0,.5,0,1), label='Histogram')
plt.plot(kde.support, kde.density, lw=3, label='KDE from samples', zorder=10)
x = np.linspace(10, 15, 100)
p = norm.pdf(x, mu, std)
print("mean = " + str(mu) + "standard dev" + str(std))
plt.plot(x, p, 'k', linewidth=2)
plt.xlim(10,15)
plt.xlabel('Execution Time')
plt.show()

