from collections import Counter
def solve(arr:list , k: int , n:int) -> int:
        arr.sort()
        if n == 1:
                return 1

        x = Counter(arr)
        count: int = 0
        t:int = n
        for items in x.items():
            if t <= 0:
                break
            if k  >= (n - items[1]):
                return 1
            t -= items[1]
            t -= k 
            count+=1
        return count

for _ in range(int(input())):
               n,k = map(int,input().split(" "))
               n_arr = list(map(int,input().split(" ")))
               print(solve(n_arr,k , n))