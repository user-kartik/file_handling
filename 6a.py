import numpy as np

#creation of array

arr1=np.array ([1,2,4,3,8,6])

arr2=np.array([[1,2,3], [8,11,9]])

arr3=np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

print(arr1)

print(arr2)

print(arr3)

#indexing

print("4th element in 1d array: \n", arr1[3])

print("2nd element in first row of 2d array\n", arr2[0,1])

print("3rd element in second row of 3d array\n", arr3 [0,1,2])

#slicing

print("slicing in 1d array:\n", arr1[0:3])

print("slicing in 2d array: \n", arr2[0:3])

print("slicing in 3d array: \n", arr3 [0:2,1:3])

#sorting

print("sorting in 1d array:\n", np.sort(arr1))

print("sorting in 2d array:\n", np.sort(arr2))

print("sorting in 3d array:\n", np.sort(arr3))

#reshaping

new_arr1=arr1.reshape(2,3)
new_arr4=np.array_split(arr1,3)

• print("splitting in id array: \n", new_arr4)

new_arr5=np.array_split(arr2,3)

print("splitting in 2d array: \n", new_arr5)

new_arr6=np.array_split(arr3,3)

print("splitting in 3d array: \n", new_arr6)

#stacking

print("stacking")

stacked-np.stack(arr3,axis=2)

print(stacked)

print("stacking")

stacked2=np.hstack(arr2)

print(stacked2)

print("\n")

stacked3=np.hstack(arr3)

print(stacked3)

stacked4=np.vstack(arr3)

print(stacked4)

stacked5=np.dstack (arr3)

print(stacked5)
