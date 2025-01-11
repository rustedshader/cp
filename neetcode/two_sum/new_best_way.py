nums = [3,5,5,6,1]
target = 7
prevMap = {}

for i,n in enumerate(nums):
    diff  = target  - n
    if diff in prevMap:
        print(prevMap[diff],i)
    prevMap[diff] = n
    print(diff,n,i, prevMap)
