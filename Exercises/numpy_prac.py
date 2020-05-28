import numpy as np

# Numpy array is homogeneous

# Implicit Declaration
ai = np.array([1, 2, 3])
af = np.array([1, 2, 3.])
ac = np.array([1j, 2, 3.])

print(ai.dtype)
print(af.dtype)
print(ac.dtype)

# Explicit Declaration
ad = np.array([1, 2, 3.], float)

# Zen Of Python - Explicit Declarations Are Better

dt = np.dtype([('value', np.int), ('status', np.bool)])
a = np.array([(1, True), (2, False)], dt)

print(a)

# array.ndim, array.size, array.size, array.dtype

o = np.ones((3, 10))
e = np.zeros((4, 5, 6), dtype=float)


