#pip install numpy
'''Numpy
it is library
is used for array
it powerful python is used to performed mathematical operation on large data
fast speed
uses less memory 
support broadcasting
does not use loops
homogenous collection
support 1d,2d,multidimensional array
built-in mathematical function

#difference between numpy array vs python list
numpy array                                     python list
faster speed                                    slower
uses less memory                                more
homogenous                                      hetergeneous
built-in mathematical function
suuports multi dimensional array                required nested list
support broadcasting                            no
types-

1)1D Array
it contain single row'''

import numpy as np
arr1=np.array([10,20,30,40,50])
print(arr1)
print(arr1.shape) #(r,) r- no of rows c- zerp

'''2) 2D Array
it contains rows and columns

'''
import numpy as np
arr2=np.array([
[1,2],
[3,4]
])
print(arr2)
print(arr2.shape) #(r,c) - (2,2)

import numpy as np
arr3=np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])
print(arr3)
print(arr3.shape)

'''3) 3D Array
it is like multiple 2D arrays stacked together (n,r,c)
n-no of 2D array , r- no of rows ,c- no of column
 n dimensional array - combination of 2D Array
'''
arr4=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[11,22,33]]
])
print(arr4)
print(arr4.dtype)

print(arr4.shape) #(n,r,c) - (2,2,3)