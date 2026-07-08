import numpy as np

arr = np.random.random((3,3))
print(arr)
arr_min = np.min(arr)
print(arr_min)
arr_max = np.max(arr)
norm_arr = (arr - arr_min) / (arr_max - arr_min)
print(norm_arr)
cumsum_arr = np.cumsum(norm_arr)
print(cumsum_arr)
cummax_arr = np.max(cumsum_arr)
print(cummax_arr)
