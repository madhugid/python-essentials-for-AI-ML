# Array: Primary data structure in NumPy, represented as homogeneous n-dimensional grid of values.

# Reshape: Transform an array into a new shape with same number of elements.

# Ravel: Flatten an array into one dimensional shape.

# Stack: Vertically or horizontally concatenate arrays.

# Slice: Extract subset of array elements using indexing.

import numpy as np

# Create array
arr = np.array([1, 2, 3]) 
print(arr)

# Reshape 
arr = arr.reshape(1, 3)
print(arr)  

# Ravel (flatten)
flattened = arr.ravel() 

# Stack vertically  
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
stacked = np.vstack([arr1, arr2])  

# Slice
sliced = arr[0:2]
