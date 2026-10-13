import numpy as np
def mk_volume() -> np.ndarray:
    a : np.ndarray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    a = np.reshape(a, (2, 2, 2))
    return a

b = 0
c = 1
d = 1
vol : np.array = mk_volume()
print(vol[b, c, d])
