#sort - display array in ascending order
import numpy as np
arr1=np.array([56,34,23,12,8,69])
s=np.sort(arr1)
print(s)

#display array in descending order
rev=s[::-1]
print(rev)

print(np.sort(arr1)[::-1])

r = np.array(sorted(arr1, reverse=True))
print(r)


import numpy as np
#S10 --- string with max 10 character

dtype=[('name','S10'),('height',float),('age',int),('gender','S10')]
values=[('shubham',5.9,43,'M'),('Arpita',5.6,23,'F'),('Vaishali',5.2,30,'F')]
x=np.array(values,dtype=dtype)
print(x)

y=np.sort(x,order='age')
print(y)

# #age --- sort---- descending order
a=np.sort(x,order='age')
print(a[::-1])