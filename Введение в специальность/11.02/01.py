import numpy as np

st = input('int arr >> ')
nums = [int(s) for s in st.split()]

v1 = np.array(nums)
v2 = np.array([nums[len(nums) - 2]])
v3 = v1[::-1]
v4 = v1[::2]
v5 = np.array(range(0, len(nums)))

print(v1, v2, v3, v4, v5)