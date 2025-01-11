n, m, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))
count = 0
matched = []
for i in arr_n:
    if i in arr_m:
        arr_m.remove(i)
        matched.append(i)
        count += 1
arr_n = [i for i in arr_n if i not in matched]

for i in arr_n:
    to_remove = False
    for z in arr_m:
        if z <= i + k and z >= i - k:
            to_remove = True
            arr_m.remove(z)
            break
    if to_remove == True:
        count+=1
print(count)
