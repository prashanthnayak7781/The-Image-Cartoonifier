Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... arr1 = np.array([[1, 2, 3, 4],
...                  [5, 6, 7, 8],
...                  [9, 10, 11, 12],
...                  [13, 14, 15, 16]])
... arr2 = np.random.uniform(low=0, high=1, size=(4, 4))
... result = arr1 * arr2
... print(result)
