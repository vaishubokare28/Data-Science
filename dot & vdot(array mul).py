# return the dot product of two vectors
#dot-  to perform matrix multiplication
import numpy as np
array1=np.array([[1,2]])
array2=np.array([[1,2],[3,4]])
result=np.dot(array1,array2)
print(result)

# [1  2]   [1 2]
#          [3 4]
# 1*1 +2*3 =7
# 1*2 +2*4=10 =[[7,10]]


#vdot - return the dot product of two vectors
a=np.array([[100,200],[23,12]])
b=np.array([[10,20],[12,21]])
vd=np.vdot(a,b)
print(vd)

#100*10+200*20+23*12+12*21=5528  element by element multiplication + addition 