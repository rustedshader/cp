# What is Insertion Sort ?

Insertion sort is an algorithm where we move from left to right and select an index and swap till starting if previous index is lesser than the current index.

For Example Code:

```python
arr = [4, 3, 2, 1]

for i in range(len(arr)):
    k = i
    while k > 0 and arr[k] < arr[k - 1]:
        arr[k], arr[k - 1] = arr[k - 1], arr[k]
        k -= 1

print(arr)
```
