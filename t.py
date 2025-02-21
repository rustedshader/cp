def solve(arr: list):
    l = arr[0]
    for i in range(len(arr)):
        if a[i] != l:
            return False
    return True

a = [1,2,3,4,5]
solve(a)
