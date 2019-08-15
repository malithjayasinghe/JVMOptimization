import subprocess
import os
import sys
sys.path.append('/Users/malithjayasinghe/JVMOptimization')
from bayes_opt import BayesianOptimization
def get_execution_time(x):
    os.environ["JAVA_OPTS"] = "-XX:NewRatio="+str(int(x))
    p = subprocess.Popen("/Users/malithjayasinghe/JVMOptimization/jvm_optimization/run_integration", shell=True, stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
    print p.returncode
    f = open("response_time.txt", "r")
    run_time = -1*float(f.readline())
    print("run time " + str(run_time) + "X = "+ str(int(x)))
    return run_time;



pbounds = {'x': (1, 100)}

optimizer = BayesianOptimization(
    f=get_execution_time,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)


optimizer.maximize(
    init_points=1,
    n_iter=50,
)

print(optimizer.max)
