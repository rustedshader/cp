# Running Time of Max Heapify: O(logn) as we call for each level and height of binary tree is LogN


def max_heapify(a, heap_size, i):
    L = 2 * i
    R = 2 * i + 1

    Largest = i

    if L < heap_size and a[L] > a[i]:
        Largest = L

    if R < heap_size and a[R] > a[Largest]:
        Largest = R

    if Largest != i:
        a[i], a[Largest] = a[Largest], a[i]
        max_heapify(a, heap_size, Largest)


# Leaves of binary Tree: A[floor(n/2) + 1] to A[n]
# Running Time: O(n)


def build_max_heap(a):
    heap_size = len(a)
    for i in range(heap_size // 2, 0, -1):
        max_heapify(a, heap_size, i)
