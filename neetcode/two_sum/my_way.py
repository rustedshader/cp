nums = [3,4,5,6]
target = 7

for i in range(0,len(nums)):
    for k in range(i+1,len(nums)):
        if nums[i] + nums[k] == target:
            print([i,k])
