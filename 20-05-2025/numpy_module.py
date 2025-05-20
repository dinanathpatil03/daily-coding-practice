# create array using numpy

## create 1D array
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))
print(arr1.shape)


arr2 = np.array([[1, 2, 3, 4, 5]])
# arr2.reshape(1, 5)
print(arr2.shape)

# 2D array
arr3 = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
# arr2.reshape(1, 5)
print(arr3)
print(arr3.shape)

# array slicing

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Array: \n", arr)
print(arr[0][3])    # 0 is number of rows and 3 is index of number from 1st row
# print(arr[1:, 2:])  # similarly slicing 1: is number of row and 2: index of number present in row
# print(arr[0:2, 2:])
print(arr[1:, 1:3])