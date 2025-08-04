import random


def quick_sort(arr, L, R):
    # Size 1 already sorted
    if R - L <= 1:
        return
    x = arr[random.randint(L, R - 1)]
    m = L
    for i in range(L, R):
        if arr[i] < x:
            arr[i], arr[m] = arr[m], arr[i]
            m += 1

    quick_sort(arr, L, m)
    quick_sort(arr, m, R)
    return arr


# Better than quicksort
def find(arr, L, R, K):
    # L <= K < R
    if R - L == 1:
        return arr[K]
    x = arr[random.randint(L, R - 1)]
    m = L
    for i in range(L, R):
        if arr[i] < x:
            arr[i], arr[m] = arr[m], arr[i]
            m += 1
    if K < m:
        return find(arr, L, m, K)
    else:
        return find(m, R, K)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(quick_sort(arr, 0, len(arr)))
