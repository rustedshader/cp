# First in First Out
from collections import deque

# Add left remove left
q = deque()

print(q)


# Enque Add element to the right
q.append(5)
q.append(3)
# Deque remove element from the left
print(q.popleft())
print(q)
