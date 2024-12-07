import numpy as np

# One dimensional array
print(f'{80 * "="}')
print('One dimensional array')
print('In: np.array([1, 2, 3]')
print(f'Out: {np.array([1, 2, 3])}')

# Two dimensional array
np_mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f'{80 * "="}')
print('Two dimensional array')
print(f'In: np.array([[1, 2, 3], [4, 5, 6]])')
print(f'Out:\n {np.array([[1, 2, 3], [4, 5, 6]])}')

# Initializing a numpy array
## Using zeros
print(f'{80 * "="}')
print('Numpy zero matrix')
print(f'In: np.zeros((3, 3))')
print(f'Out:\n {np.zeros((3, 3))}')

## Arranging numbers between x and y with interval of z
print(f'{80 * "="}')
print('Numpy arange')
print(f'In: np.arange(10, 25, 5)')
print(f'Out: {np.arange(10, 25, 5)}')
print(f'{80 * "-"}')
print(f'In: np.arange(10, 20, 2)')
print(f'Out: {np.arange(10, 20, 2)}')

## Arranging z numbers between x and y
print(f'{80 * "="}')
print('Numpy linspace')
print(f'In: np.linspace(10, 20, 10)')
print(f'Out:\n {np.linspace(10, 20, 10)}')

## Filling same number in an array of dimension x cross y
print(f'{80 * "="}')
print('Numpy full')
print(f'In: np.full(2, 2), 5)')
print(f'Out:\n {np.full((2, 2), 5)}')
print(f'{80 * "-"}')
print(f'In: np.full(2, 4), 6)')
print(f'Out:\n {np.full((2, 4), 6)}')

## Filling random numbers in an array of dimension x cross y
print(f'{80 * "="}')
print('Numpy random')
print(f'In: np.random.random((2, 2))')
print(f'Out:\n {np.random.random((2, 2))}')
