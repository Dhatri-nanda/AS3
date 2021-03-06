# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qNVBCoE2Mx1UE5MZHq01eb03FhpnHJsZ
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from random import choices
import subprocess
import shlex


X=[1, 2, 3] 
pr_dis_red=[2/9, 4/9, 3/9]
pr_dis_green=[3/9, 3/9, 3/9]
pr_dis_blue=[3/9, 4/9, 2/9]

simlen = 100000

#for the two outcomes to be red
prob_r = 3/10
#generating data for first draw
data_bern_r = bernoulli.rvs(size=simlen,p=prob_r)
#generating data for second draw
b1=[1]*(simlen)
for i in range(simlen):
    if (data_bern_r[i] == 1) :
       b1[i]=random.choices(X,pr_dis_red)      
num_red=b1.count([1])
pr_red=num_red/simlen

#for the two outcomes to be green
prob_g = 4/10
#generating data for first draw
data_bern_g = bernoulli.rvs(size=simlen,p=prob_g)
b2=[2]*(simlen)
#generating data for second draw
for i in range(simlen):
    if (data_bern_g[i] == 1) :
       b2[i]=random.choices(X,pr_dis_green)       
num_green=b2.count([2])
pr_green=num_green/simlen

#for the two outcomes to be blue
prob_b = 3/10
#generating data for first draw
data_bern_b = bernoulli.rvs(size=simlen,p=prob_b)
#generating data for second draw
b3=[3]*(simlen)
for i in range(simlen):
    if (data_bern_b[i] == 1) :
       b3[i]=random.choices(X,pr_dis_blue)       
num_blue=b3.count([3])
pr_blue=num_blue/simlen

print("simulated probability is", pr_red+pr_green+pr_blue)
print("That is approximately equal to the theoritical probability of 0.267")

cases = ["x = 1"]
prob_T = [6/90+ 12/90+ 6/90]
prob_S = [pr_red+ pr_green+pr_blue]

x = np.arange(len(cases))
plt.stem(x + 0.00, prob_T, markerfmt='o',use_line_collection=True, basefmt=None , linefmt='orange' ,label='Theoritical')
plt.stem(x + 0.25, prob_S, markerfmt='o', use_line_collection=True, basefmt=None  ,linefmt='b', label='Simulated')
plt.xlabel('cases')
plt.ylabel('Probability')
plt.xticks(x + 0.25/2,[1])
plt.legend()
plt.grid()
plt.show()