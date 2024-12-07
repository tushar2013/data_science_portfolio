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

###############################################################################

# Subtracting the elements of an array
print(f'{80 * "="}')
print('###### Subtracting the elements of an array ######')
np_subtract_mat_one = np.array([[1, 2, 3], [10, 11, 12]])
np_subtract_mat_two = np.array([[7, 8, 9], [4, 5, 6]])
print(f'np_subtract_mat_one\n{np_subtract_mat_one}')
print(f'np_subtract_mat_two\n{np_subtract_mat_two}')

print(f'In: np.subtract(np_subtract_mat_one, np_subtract_mat_two)')
print(f'Out:\n {np.subtract(np_subtract_mat_one, np_subtract_mat_two)}')

#print(f'{80 * "-"}')
#np_subtract_mat = np.array([[1, 2, 3], [4, 5, 6]])
#print('Cmd: np_subtract_mat = np.array([[1, 2, 3], [4, 5, 6]]')
#print('In: np.subtract(np_subtract_mat, axis=0)')
#print(f'Out: {np.subtract(np_subtract_mat, axis=0)}')
#
#print(f'{80 * "-"}')
#np_subtract_mat = np.array([[1, 2, 3], [4, 5, 6]])
#print('Cmd: np_subtract_mat = np.array([[1, 2, 3], [4, 5, 6]]')
#print('In: np.subtract(np_subtract_mat, axis=1)')
#print(f'Out: {np.subtract(np_subtract_mat, axis=1)}')
