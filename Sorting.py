from array import *
import random

#Define Array
Arr = array('i',[])

#Assign number to Arr using ramdom function
for x in range(5):
    Arr.append(random.randint(0,100))

#Print Generated Array
print('Generated Array: ', end="")
for y in Arr:
    print(y,end="  ")
print()

#Sorting Process
for i in range(len(Arr)):
    test = Arr[i]
    for j in range(i+1,len(Arr)):
        if test > Arr[j]:
            Arr[i] = Arr[j]
            Arr[j] = test
            test = Arr[i]

#Print Sorted Array
print('Sorted Array   : ', end="")
for z in Arr:
    print(z,end="  ")
print()

