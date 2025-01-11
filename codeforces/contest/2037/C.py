def isComposite(n: int) -> bool:
    if n <= 3:
        return False
    if n % 2 == 0:
        return True

    for i in range(2, int((n**0.5) + 1)):
        if n % i == 0:
            return True

    return False


def solve(n: int):
    # As sum of two composite number is minimum 8  4+4
    if n <= 7:
        return [-1]

    # Precompute composites till 2n
    precomputed_arr = [k for k in range(1,n+1)]


    max_comp = 2 * n
    comp = [False] * (max_comp + 1)
    for i in range(4, (max_comp + 1)):
        comp[i] = isComposite(i)

    ans = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if comp[i + j] and i != j :
                    ans.append(i)
                    ans.append(j)
    ans2 = []
    for k in range(len(ans) - 1):
        if isComposite(ans[k] + ans[k+1]):
            ans2.append(k)
            ans2.append(k+1)
            

    return ans2


for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    print(*ans)
