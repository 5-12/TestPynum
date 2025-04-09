import numpy as np
dt=np.dtype([("n1","i4"),
             ("n2","i4")
             ])
test=np.array([[(1 , 2 ),( 3 , 4 )],[( 5 , 6 ),( 7 , 8 )]],dtype=dt)
# np.ndarray
print(test.itemsize)
print(test.ndim)
print(test.shape)
print(test)
print()
test1=test.reshape((4,1))
print(test1.itemsize)
print(test1.ndim)
print(test1.shape)
print(test1)