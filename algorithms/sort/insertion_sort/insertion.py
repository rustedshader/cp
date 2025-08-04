def insertion_sort(arr: list):
    for i in range(len(arr)):
        k = i
        while k > 0 and arr[k] < arr[k - 1]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1
    return arr


if __name__ == "__main__":
    x = [2, 45, 64, 32, 233, 4242, 34, 3, 3]
    print(insertion_sort(x))
