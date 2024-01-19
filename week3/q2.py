import numpy as np  
a=np.arange(12).reshape(3,4)
c1=np.sum(a,axis=1)
r1=np.sum(a,axis=0)
print(c1)
print(r1)