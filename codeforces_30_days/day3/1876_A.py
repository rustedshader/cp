def solve(a_arr: list[int], b_arr: list[int], n: int, p: int):
    if p < min(b_arr):  # If all elements in b_arr are more expensive than p
        return p * n
    if n == 1:  # Edge case for a single element
        return p

    t = n
    cost: int = 0

    # Sort by b_arr ascending, and if equal, sort by a_arr descending
    pairs = sorted(zip(b_arr, a_arr), key=lambda x: (x[0], -x[1]))
    b_arr = [x[0] for x in pairs]
    a_arr = [x[1] for x in pairs]

    i = 0
    while t > 0 and i < n:
        if a_arr[i] <= t:  # If we can buy all of this item
            cost += b_arr[i] * a_arr[i]
            t -= a_arr[i]
        else:  # If we can only partially buy this item
            cost += b_arr[i] * t
            t = 0
        i += 1

    # If there are remaining items, add penalty cost
    cost += p * t
    return cost


# Input and Test Cases
for _ in range(int(input())):
    n, p = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    print(solve(a_arr, b_arr, n, p))