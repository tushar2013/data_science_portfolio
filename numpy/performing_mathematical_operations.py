import numpy as np

###############################################################################

# Summing the elements of an array
print(f'{80 * "="}')
print('###### Summing the elements of an array ######')
np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Cmd: np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]]')
print(f'In: np.sum(np_sum_mat)')
print(f'Out: {np.sum(np_sum_mat)}')

print(f'{80 * "-"}')
np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Cmd: np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]]')
print(f'In: np.sum(np_sum_mat, axis=0)')
print(f'Out: {np.sum(np_sum_mat, axis=0)}')

print(f'{80 * "-"}')
np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Cmd: np_sum_mat = np.array([[1, 2, 3], [4, 5, 6]]')
print(f'In: np.sum(np_sum_mat, axis=1)')
print(f'Out: {np.sum(np_sum_mat, axis=1)}')

print(f'{80 * "-"}')
print('###### Summing two arrays ######')
np_subtract_mat_one = np.array([[1, 2, 3], [10, 11, 12]])
np_subtract_mat_two = np.array([[7, 8, 9], [4, 5, 6]])
print(f'np_subtract_mat_one\n{np_subtract_mat_one}')
print(f'np_subtract_mat_two\n{np_subtract_mat_two}')

print(f'In: np.sum(np_subtract_mat_one, np_subtract_mat_two)')
print(f'Out:\n {np_subtract_mat_one + np_subtract_mat_two}')

###############################################################################

# Subtracting the elements of an array
print(f'{80 * "="}')
print('###### Subtracting two arrays ######')
np_subtract_mat_one = np.array([[1, 2, 3], [10, 11, 12]])
np_subtract_mat_two = np.array([[7, 8, 9], [4, 5, 6]])
print(f'np_subtract_mat_one\n{np_subtract_mat_one}')
print(f'np_subtract_mat_two\n{np_subtract_mat_two}')

print(f'In: np.subtract(np_subtract_mat_one, np_subtract_mat_two)')
print(f'Out:\n {np.subtract(np_subtract_mat_one, np_subtract_mat_two)}')

###############################################################################

# Multiplying the elements of an array
print(f'{80 * "="}')
print('###### Multiplying two arrays ######')
np_multiply_mat_one = np.array([[1, 2, 3], [10, 11, 12]])
np_multiply_mat_two = np.array([[7, 8, 9], [4, 5, 6]])
print(f'np_multiply_mat_one\n{np_multiply_mat_one}')
print(f'np_multiply_mat_two\n{np_multiply_mat_two}')

print(f'In: np.multiply(np_multiply_mat_one, np_multiply_mat_two)')
print(f'Out:\n {np.multiply(np_multiply_mat_one, np_multiply_mat_two)}')

###############################################################################

# Dividing the elements of an array
print(f'{80 * "="}')
print('###### Dividing two arrays ######')
np_divide_mat_one = np.array([[1, 2, 3], [10, 11, 12]])
np_divide_mat_two = np.array([[7, 8, 9], [4, 5, 6]])
print(f'np_divide_mat_one\n{np_divide_mat_one}')
print(f'np_divide_mat_two\n{np_divide_mat_two}')

print(f'In: np.divide(np_divide_mat_one, np_divide_mat_two)')
print(f'Out:\n {np.divide(np_divide_mat_one, np_divide_mat_two)}')

###############################################################################

# Other  Mathematical operators and functions in numpy
print(f'{80 * "="}')
print('###### Other  Mathematical operators and functions in numpy ######')
np_other_mat = np.arange(6)
print(f'Cmd: np_other_mat = np.arange(6)')
print(np_other_mat)

print(f'{80 * "-"}')
print(f'In: np.exp(np_other_mat)')
print(f'Out:\n {np.exp(np_other_mat)}')

print(f'{80 * "-"}')
print(f'In: np.sin(np_other_mat)')
print(f'Out:\n {np.sin(np_other_mat)}')

print(f'{80 * "-"}')
print(f'In: np.cos(np_other_mat)')
print(f'Out:\n {np.cos(np_other_mat)}')

print(f'{80 * "-"}')
print(f'In: np.log(np_other_mat)')
print(f'Out:\n {np.log(np_other_mat)}')
