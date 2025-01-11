def linear_search(arr,to_find):
    i = 0
    while(i<len(arr)-1):
        if arr[i] == to_find:
            return i
        i+=1
    return "Not Found !"
arr = [1,34,52,1231,5252,311,3214,121]
print(linear_search(arr,311))
