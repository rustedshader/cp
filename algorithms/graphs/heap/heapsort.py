def heap_sort(arr):
    arr = build_max_heap(arr)
    heap_size = len(arr)

    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heap_size -= 1

        heapify(arr, heap_size, 0)
    return arr


def build_max_heap(arr):
    heap_size = len(arr)

    for i in range((heap_size // 2) - 1, -1, -1):
        heapify(arr, heap_size, i)
    return arr


def heapify(arr, heap_size, i):
    max_idx = i
    L = (2 * i) + 1
    R = (2 * i) + 2

    if L < heap_size and arr[L] > arr[max_idx]:
        max_idx = L

    if R < heap_size and arr[R] > arr[max_idx]:
        max_idx = R

    if i != max_idx:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        heapify(arr, heap_size, max_idx)
    return arr


if __name__ == "__main__":
    arr = [2, 8, 5, 3, 9, 1]
    print(heap_sort(arr))
