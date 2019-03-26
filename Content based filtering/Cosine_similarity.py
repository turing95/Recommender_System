# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:25:15 2019

@author: marco
"""

#defined as sum(A*B)/|A|*|B|

import numpy as np

a=([1,2,3])
b=([1,1,4])

dot = np.dot(a,b)
norma=np.linalg.norm(a)
normb=np.linalg.norm(b)

cos=dot/(norma*normb)

print(cos)
