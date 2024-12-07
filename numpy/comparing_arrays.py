import numpy as np

np_equal_array_one = np.array([1, 2, 3])
np_equal_array_two = np.array([1, 2, 3])
np_equal_array_three = np.array([4, 5, 3])

print(np.equal(np_equal_array_one, np_equal_array_two))
print(np.equal(np_equal_array_one, np_equal_array_three))
