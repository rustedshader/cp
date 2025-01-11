def binary_search(arr,to_find,high,low):
    middle = (high + low) // 2
    while(high-low > 1):
        if(to_find > arr[middle]):
            low = middle + 1
            middle = (low+high) // 2
        else:
            high = middle
            middle = (low+high) // 2
    if (to_find == arr[high]):
        return high
    elif (to_find == arr[low]):
        return low
    else:
        return "Number not Found !"


x = [1,24,26,51,256,431,652]
print(binary_search(x,24,6,0))
