import numpy as np
# x=np.array([1,2,3])
# print(x)
# print("Type:",type(x))
#-----1D ARRAY.....
arr=np.array([1,2,3,4,5])
print(arr)
#-----2D ARRAY.....
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
#-----3D ARRAY.....
arr2=np.array([[[1,2,3],[4,5,6]]])
print(arr2)
#----ARRAY OPERATION---
array=np.array([[1,2,3],[4,5,6]])
print("Data_type:",array.dtype)
print("Shape:",array.shape)
print("size:",array.size)
print("Dimention:",array.ndim)
print("non_zeros:",np.count_nonzero(array))
print("max:",array.max())
print("min:",array.min())
print(np.where(array>5))
#---reshape---
arr3=np.array([1,2,3,4,5,6])
x=arr3.reshape(3,2)
print(x)
#---special numpy array---
print(np.zeros((3,4)))
print(np.empty((2,3)))
print(np.arange(4))
#---Numpy by DIAGONAL---
print(np.eye(3))
print(array.sum(axis=0))
print(array.sum(axis=1))
#----ARITHMETIC OPERATION--
#------1D----
arr4=np.array([1,2,3,4])
arradd=arr4+5
print(arradd)
arr5=np.array([1,2,3,4])
arr6=np.array([5,6,7,8])
arradd1=arr5+arr6
print(arradd1)
#------2D----
arr7=np.array([[1,2,3,4],[5,6,7,8]])
arr8=np.array([[1,2,3,4],[5,6,7,8]])
print("ADD:",np.add(arr7,arr8))
print("SUBTRACT",np.subtract(arr7,arr8))
print("Multiplication",np.multiply(arr7,arr8))
print("DIVIDE:",np.divide(arr7,arr8))
#---Brodcasting numpu----
arr9=np.array([1,2,3])
arr10=np.array([[1],[2],[3]])
print("Sum of 1D and 2D array:\n",arr9+arr10)
#---indexing and slicing----
arr11=np.array([1,2,3,4])
print(arr11[-3])
print("2 to 4:",arr11[1:5])
arr12=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr12[1,0])
print("4 to 6:",arr12[1,0:3])
