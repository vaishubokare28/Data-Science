import numpy as np
a=np.random.randint(3,size=10) #random number generate
print(a)

# # print(a) #3- 0 1 2 size=10 means 10 elements
# # #[2 0 0 0 1 1 0 0 1 2]
# # #a=np.random.randint(8,size=10) 

# #display 5 times false ---True kabhi bhi nahi ayegi 
a=np.random.randint(True,size=5,dtype=np.bool)
print(a) #[False False False False False]

a=np.random.randint(True,size=5)
print(a)#[0 0 0 0 0]