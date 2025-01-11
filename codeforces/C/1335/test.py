def b_search(arr,to_find):
    min = 0
    max = len(arr)
    m = max // 2
    while(max-min > 1):
        if (to_find >  arr[m]):
            min = m + 1
            m = (min + max) // 2
        else:
            max = m
            m = (min + max) // 2
    if arr[min] == to_find:
        return min
    elif arr[max] == to_find:
        return max
    else:
        return "Not found !"

print(b_search([1,2,3,4,5,6,7],6))
