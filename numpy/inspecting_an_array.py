import numpy as np

###############################################################################

# Shape of an array
print(f'{80 * "="}')
print('Numpy shape')
print('In: np.array([1, 2, 3].shape')
print(f'Out: {np.array([1, 2, 3]).shape}')
print(f'{80 * "-"}')
print(f'In: np.array([[1, 2, 3], [4, 5, 6]]).shape')
print(f'Out: {np.array([[1, 2, 3], [4, 5, 6]]).shape}')

###############################################################################

# Resizing an array
print(f'{80 * "="}')
print('###### Resizing an array ######')
np_shape_mat = np.array([[1, 2, 3], [4, 5, 6]])
print('Cmd: np_shape_mat = np.array([[1, 2, 3], [4, 5, 6]]')
print('In: np_shape_mat')
print(f'Out:\n {np_shape_mat}')

print(f'{80 * "-"}')
print('====== Checking the shape  ======')
print('In: np_shape_mat.shape')
print(f'Out: {np_shape_mat.shape}')

print(f'{80 * "-"}')
print('====== Reshaping/Resizing the array  ======')
np_shape_mat.shape = (3, 2)
print(f'Cmd: np_shape_mat.shape = (3, 2)')
print(f'In: np_shape_mat')
print(f'Out:\n {np_shape_mat}')
print(f'Out:\n {np_shape_mat.ndim}')

print(f'{80 * "-"}')
print('====== Checking the shape  ======')
print('In: np_shape_mat.shape')
print(f'Out: {np_shape_mat.shape}')

print(f'{80 * "-"}')
print('====== Reshaping/Resizing the array  ======')
np_shape_mat.shape = (6, 1)
print(f'Cmd: np_shape_mat.shape = (6, 1)')
print(f'In: np_shape_mat')
print(f'Out:\n {np_shape_mat}')

###############################################################################

# Check dimension of an array
print(f'{80 * "="}')
print('###### Check dimension of an array ######')
np_ndim_mat = np.array([[1, 2, 3], [4, 5, 6]])
print('Cmd: np_ndim_mat = np.array([[1, 2, 3], [4, 5, 6]]')

print(f'{80 * "-"}')
print(f'In: np_ndim_mat')
print(f'Out:\n {np_ndim_mat}')

print(f'{80 * "-"}')
print('In: np_ndim_mat.ndim')
print(f'Out: {np_ndim_mat.ndim}')

###############################################################################

# Reshaping an array
print(f'{80 * "="}')
print('###### Reshaping an array ######')
np_reshape_mat = np.arange(30)
print(f'Cmd: np_reshape_mat = np.arange(30)')

print(f'{80 * "-"}')
print(f'In: np_reshape_mat')
print(f'Out:\n {np_reshape_mat}')

print(f'{80 * "-"}')
print(f'In: np_reshape_mat.reshape(5, 6)')
print(f'Out:\n {np_reshape_mat.reshape(5, 6)}')

print(f'{80 * "-"}')
print(f'In: np_reshape_mat.reshape(15, 2)')
print(f'Out:\n {np_reshape_mat.reshape(15, 2)}')

print(f'{80 * "-"}')
print(f'In: np_reshape_mat.reshape(2, 3, 5)')
print(f'Out:\n {np_reshape_mat.reshape(2, 3, 5)}')

###############################################################################

# Finding elements of an array
print(f'{80 * "="}')
print('###### Finding elements of an array ######')
np_size_mat = np.arange(9)
np_size_mat = np_size_mat.reshape(3,3)
print(f'In: np_size_mat')
print(f'Out:\n {np_size_mat}')

print(f'{80 * "-"}')
print(f'In: np_size_mat.size')
print(f'Out: {np_size_mat.size}')

# Throws error
#print(f'{79 * "-"}')
#np_size_uneven_mat = np.array([[1,2,3], [4,5,6], [7,8,9,10]])
#print(f'In: np_size_uneven_mat.size')
#print(f'Out: {np_size_uneven_mat.size}')

###############################################################################

# Finding the datatype of an array
print(f'{80 * "="}')
print('###### Finding the datatype of an array ######')
np_dtype_mat = np.arange(10, dtype=float)
print(f'Cmd: np_dtype_mat = np.arange(10, dtype=float)')
print(f'In: np_dtype_mat.dtype')
print(f'Out: {np_dtype_mat.dtype}')

print(f'{80 * "-"}')
np_dtype_mat = np.arange(10)
print(f'Cmd: np_dtype_mat = np.arange(10)')
print(f'In: np_dtype_mat.dtype')
print(f'Out: {np_dtype_mat.dtype}')
