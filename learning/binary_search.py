def binary_search(arr: list, to_find: int) -> int | None:
    L = 0
    R = len(arr)
    while L <= R:
        middle: int = L + ((R - L) // 2)
        if to_find < arr[middle]:
            R = middle - 1
        elif to_find > arr[middle]:
            L = middle + 1
        else:
            return middle
    return None


arr = [1, 4, 5, 7, 9]

print(binary_search(arr, 9))
