nums = [3,5,5,6,1]
target = 7
prevMap = {}  # val -> index

for i, n in enumerate(nums):
    diff = target - n
    print(diff,prevMap)
    if diff in prevMap:
        print(prevMap[diff],i)
    prevMap[n] = i

print(prevMap)
