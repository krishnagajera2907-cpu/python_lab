from array import array
arr = array('i',[10,20,30,40,50])
print(arr[1:4]) #index 1 to 3
print(arr[:3]) #start to index 2
print(arr[2:]) #index 2 to end
print(arr[:]) #entire array

from array import array
arr = array('i',[10,20,30,40,50,60,70,80])
print(arr[::2]) #every second element
print(arr[1::2]) #every second element starting from index 1
print(arr[::3]) #every third element

from array import array
arr = array('i',[10,20,30,40,50])
print(arr[-4:-1]) #from index -4 to -2
print(arr[-3:]) #last three elements
print(arr[:-2]) #all except last two

from array import array
arr = array('i',[10,20,30,40,50])
arr[1:4] = array('i',[25,35,45])
print(arr)