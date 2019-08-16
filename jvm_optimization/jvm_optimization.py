import subprocess
import os
import sys
from matplotlib import pylab as plt
import statsmodels.api as sm

sys.path.append('/Users/malithjayasinghe/JVMOptimization')
from bayes_opt import BayesianOptimization
execution_times_opt = []
warm_up = 20
count = 0
num_iterations  = 50
from scipy.stats import shapiro

def get_execution_time(x):
    global count
    os.environ["JAVA_OPTS"] = "-XX:NewRatio="+str(int(x))
    p = subprocess.Popen("/Users/malithjayasinghe/JVMOptimization/jvm_optimization/run_integration", shell=True, stdout=subprocess.PIPE)
    for line in p.stdout:
        print (line)
    p.wait()
    print (p.returncode)
    f = open("response_time.txt", "r")
    run_time = -1*float(f.readline())

    print("run time " + str(run_time) + "X = "+ str(int(x)))
    if count > warm_up:
        execution_times_opt.append(run_time*-1.0)

    count = count + 1
    return run_time;


#from pyqt_fit import kde
execution_times = []
for x in range(num_iterations):
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
plt.hist(execution_times, bins=30, normed=True, color=(0,.5,0,1), label='Histogram')
#plt.plot(execution_times, ys, 'r--', linewidth=2, label='$\mathcal{N}(0,1)$')
plt.plot(kde.support, kde.density,'bs', label='without tunning', zorder=10)


pbounds = {'x': (1, 100)}

optimizer = BayesianOptimization(
    f=get_execution_time,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

optimizer.maximize(
    init_points=1,
    n_iter=num_iterations,
)

kde2 = sm.nonparametric.KDEUnivariate(execution_times_opt)
kde2.fit() # Estimate the densities
plt.hist(execution_times_opt, bins=30, normed=True, color=(1,.5,1,0.5), label='Histogram')
#plt.plot(execution_times, ys, 'r--', linewidth=2, label='$\mathcal{N}(0,1)$')
plt.plot(kde2.support, kde2.density, 'r--', label='with tunning', zorder=10)
plt.xlim(10,16)
plt.xlabel('Execution Time')
plt.show()
