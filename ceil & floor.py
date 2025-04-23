import numpy as np
a=np.array([1.3,4.3,3.1])
a=np.ceil(a)  #ceil-round up value  
print(a) #[2. 5. 4.]

a=np.array([1.3,4.3,3.1])
a=np.floor(a)  #floor-return int value only not show decimal values  
print(a) #[ 1.  4.  3.]

# # print(list+10)
# # print(list**2)

#to perform square of every elements and add 10 to it.
import numpy as np
a=np.array([2,3,4])
s=a**2 #[4,9,16]
print(s+10)#[14,10,26]

# list=[2,3,4,5,6]
# for i in list:
#     print(i+10)
    
a=np.array([1,2,3])
result=a+10
print(result)#[11 12 13]