def insertion_sort(l:list):
    ll_n = len(l)
    for i in range(1, ll_n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

if __name__ == "__main__":
    x = [2,45,64,32,233,4242,34,3,3]
    print(insertion_sort(x))