nums = [1, 2, 3, 3]
duplic = 0
for num in nums:
    if nums.count(num) > 1:
        duplic += 1

if duplic > 0:
    print("true")
