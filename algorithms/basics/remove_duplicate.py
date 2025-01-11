def binary_search(arr,N,to_search):
    high = N-1
    low = 0
    m = N//2
    while(high - low > 1):
        if to_search > arr[m]:
            low = m+1
            m = low + high // 2
        else:
            high = m
            m = low + high // 2
    if arr[low] == to_search:
        return low
    elif arr[high] == to_search:
        return high
    else:
        return "Not Found !"
print(binary_search([1,2,3,4,5],5,3))
