from math import ceil, floor

nums1 = [1, 3]
nums2 = [2]
final_arr = sorted(nums1 + nums2)
size_f = len(final_arr)
if size_f % 2 != 0:
    print(final_arr[size_f // 2])
else:
    print((final_arr[ceil(size_f / 2)] + final_arr[floor((size_f - 1) / 2)]) / 2)
