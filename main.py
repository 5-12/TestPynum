import numpy as np
dt=np.dtype([('n1','i4'),('n2','i4')])
test=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
print(test)
test1=np.asarray(test,dtype=dt)
print(test1)