
#vectorize opearation
'''sum=0
l=[10,20,30,40,50]
for i in l:
    sum=sum+i
    print(sum)'''

#sum - sum of all elements without for loop
import numpy as np
a=np.array([10,20,30,40,50])
res=np.sum(a)
print(res) 

#max - return max elemnt
arr1=np.array([56,34,23,12,8,69])
m=np.max(arr1)
print(m)

#max - return min element
m2=np.min(arr1)
print(m2)

#sort - display array in ascending order
s=np.sort(arr1)
print(s)

#display array in descending order
rev=s[::-1]
print(rev)

print(np.sort(arr1)[::-1])

r = np.array(sorted(arr1, reverse=True))
print(r)
