import numpy as np
print("Priting a string multiple times")
print(np.char.multiply("python",3))#pythonpythonpython

print(np.char.capitalize("welcome to numpy")) #Welcome to numpy
print(np.char.title("welcome to numpy"))  #Welcome To Numpy
print(np.char.upper("numpy")) #NUMPY
print(np.char.lower("NUMPY"))#numpy
print(np.char.strip("    NUMPY    ")) #remove space of begining and end
print(np.char.split("Python is easy language",sep=" ")) #['Python', 'is', 'easy', 'language']
print(np.char.split("12/05/2023",sep="/")) #['12', '05', '2023']






