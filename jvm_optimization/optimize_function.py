import subprocess
import os
import numpy as np
import sys
sys.path.append('/Users/malithjayasinghe/BayesianOptimization/')

def black_box_function(x):
    print(x)
    #return -1*0.01*x*x
    return -1.0*np.sin(x/5.0)*x

from bayes_opt import BayesianOptimization

pbounds = {'x': (60, 100)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)


optimizer.maximize(
    init_points=1,
    n_iter=200,
)

print(optimizer.max)
