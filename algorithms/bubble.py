def bubble_sort(l: list):
    ll_n = len(l)
    for i in range(ll_n):
        for k in range(ll_n - 1 - i):
            if l[k] > l[k+1]:
                l[k],l[k+1] = l[k+1],l[k]  
    return l

x = [2,45,64,32,233,4242,34,3,3]
print(bubble_sort(x))
