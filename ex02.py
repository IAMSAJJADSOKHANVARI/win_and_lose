#import library
import numpy as np
#Enter your number for create array
Input = int(input("please Enter your number:  "))
print("Input:",Input)
#sart to bear random number 0-100  and then create array Input 
arr = np.random.randint(0, 101, Input)
print("Array:",arr)
max_value = np.max(arr)
print("Max: ", max_value)
#use methode np.where for detect win or fail 
result = np.where(max_value > 70, "Win", "Fail")
print(result)
