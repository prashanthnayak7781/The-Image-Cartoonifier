import numpy as np
... lst = [[1, 2, 3, 4],
...        [5, 6, 7, 8],
...        [9, 10, 11, 12],
...        [13, 14, 15, 16]]
... arr = np.array(lst)
... diagonal = np.diag(arr)
... print("Diagonal elements:", diagonal)
... trace = np.trace(arr)
... print("Trace:", trace)
... max_per_row = np.max(arr, axis=1)
... min_per_row = np.min(arr, axis=1)
... print("Max per row:", max_per_row)
... print("Min per row:", min_per_row)
