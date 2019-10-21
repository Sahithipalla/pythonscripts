import numpy as np
 
my_list=[1,2,3,4,5]
np.eye(4)
np.random.rand(4)
np.random.randn(5)
arr=np.arange(36)
arr
arr.shape
arr.reshape(6,6)
ar=np.random.randint(0,33,7)
ar
ar.max()
ar.min()
ar.argmax()
ar.argmin()

ar=np.arange(8,72)
ar
slice_ar=ar[0:25]
slice_ar
slice_ar[:]=99
slice_ar
ar_cp=ar.copy()
ar_cp
ar_cp[0:25]=100
ar_cp
ar
arr=np.array([[1,2,3],[2,6,8]])
arr
arr[1][2]
arr[1,0]
ar=np.array([[12,3,4,8],[2,4,6,7]])
ar
ar[0:3,1:3]

