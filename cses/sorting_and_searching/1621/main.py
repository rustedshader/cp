import sys
n = int(sys.stdin.readline())
arr = sys.stdin.read().split()
unique_elements = set()
for num in arr:
    unique_elements.add(num)
print(len(unique_elements))
