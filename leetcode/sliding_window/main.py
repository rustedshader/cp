# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# nums = [7, 2, 4]
# k = 2

# nums = [5, 3, 4]
# k = 1


# nums = [1, -1]
# k = 1

# nums = [1, 3, 1, 2, 0, 5]
# k = 3

from collections import deque


def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()  # Deque to store indices
    ans = []  # List to store maximums

    for i in range(len(nums)):
        # Remove indices outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Record maximum once window is fully formed
        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans


print(maxSlidingWindow(nums, k))
