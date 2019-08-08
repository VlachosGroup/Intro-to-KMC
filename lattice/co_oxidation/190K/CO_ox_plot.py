# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:23:10 2019

@author: jake_
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sites = 2304
f = open('specnum_output.txt', 'r')
data = []
for l in f:
    in_list = l.strip().split()
    data.append(in_list)
data = data[1:]

t = []
CO_on = []
O_on = []
for i in data:
    t.append(float(i[2]))
    CO_on.append(float(i[5]))
    O_on.append(float(i[6]))

t = np.array(t)
CO_on = np.array(CO_on)
O_on = np.array(O_on)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,O_on/sites,'r',label = 'O');
ax.plot(t,CO_on/sites,'b',label = 'CO');
ax.plot(t,(CO_on+O_on)/sites,'k',label = 'TOT');
ax.set_title('T=190K')
ax.set_xlabel('Time[s]')
ax.set_ylabel('Coverage(O,CO)[ML]')
ax.legend()
fig.savefig('CO_ox_190.png')

