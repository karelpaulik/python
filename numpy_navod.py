NUMPY
--------------------------------------------
pip install numpy
--------------------------------------------
                Check version
import numpy as np
print(np.__version__)
--------------------------------------------
import numpy as np

#1-D array
#2-D array
#3-D array
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a)

#Check Number of Dimensions?
print(b.ndim)   #2
#Shape of an Array
print(b.shape)  #(2,3)

#generování řady
x = np.arange(0, 6.28, 0.1)   # start,stop,step
y = np.sin(x)

#pozn:
import matplotlib.pyplot as plt
plt.plot(x,y)
plt(show)

#Numpy indexing
arr = np.array([1, 2, 3, 4])
print(arr[0])   #1

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4]) #10

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6

#Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) 

#Slicing arrays: [start:end] nebo [start:end:step]
#POZOR: start index - INCLUDE, end index EXCLUDE
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2 3 4 5] 
print(arr[4:])  #[5 6 7] 
print(arr[:4])  #[1 2 3 4] 
print(arr[-3:-1])   #[5 6]

#copy(opravdu kopie)/View(pouze reference, tzn. při změně jednoho pole se změní i to druhé) pole
a = np.array([1, 2, 3, 4, 5])
b = a.copy()
a[0] = 6
print(a)    #[6 2 3 4 5]
print(b)    #[1 2 3 4 5]

#view
a = np.array([1, 2, 3, 4, 5])
b = a.view()
a[0] = 6
print(a)    #[6 2 3 4 5]
print(b)    #[6 2 3 4 5]

#Kontrola, jestli pole má svá vlastní data (jestli bylo copy/view)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)   #None
print(y.base)   #[1 2 3 4 5] 

#reshape
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = arr.reshape(4, 3)
print(b) 
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
 
 #Iterating array
 arr = np.array([1, 2, 3])

for var in arr:
  print(var)

for i, x in enumerate(arr):
  print(i, x)

for i, x in np.ndenumerate(arr):
  print(i, x)
  
1
2
3

0 1
1 2
2 3

(0,) 1
(1,) 2
(2,) 3

#Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)
arr = np.hstack((arr1, arr2))
print(arr)
arr = np.vstack((arr1, arr2))
print(arr)
arr = np.dstack((arr1, arr2))
print(arr)

[1 2 3 4 5 6]

[1 2 3 4 5 6]

[[1 2 3]
 [4 5 6]]
 
[[[1 4]
  [2 5]
  [3 6]]]
  
#Splitting NumPy Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2]) 

[1 2]
[3 4]
[5 6]

#sort array
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) 

[0 1 2 3]

nebo:
arr.sort()

#Pozn. sort u obyčejného pole:
x=[2,1,3]
x.sort()
print(x) #[1,2,3]