from collections import deque

nums = [1, 3, 1, 2, 0, 5]
k = 3
ans = []
q = deque()
for i in range(len(nums)):
    while q and q[0] < i - k + 1:
        q.popleft()

    while q and nums[i] > nums[q[-1]]:
        print("Removed", q[-1], i)
        q.pop()

    q.append(i)

    if i >= k - 1:
        ans.append(nums[q[0]])
print(ans)
