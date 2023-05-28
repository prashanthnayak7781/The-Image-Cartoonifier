Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import pandas as pd
... 
... class SortedArray:
...     def __init__(self):
...         self.array = np.array([])
... 
...     def get_array(self, length):
...         self.array = np.array([int(input(f"Enter element {i+1}: ")) for i in range(length)])
...         sorted_array = np.sort(self.array)
...         return pd.Series(sorted_array)
