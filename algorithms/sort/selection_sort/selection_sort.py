def selection_sort(arr,N):
    for i in range(N):
        min_index = i
        for k in range(i+1,N):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[min_index] , arr[i] = arr[i] , arr[min_index]
    return arr
x = [5,4,3,2,1]
print(selection_sort(x,len(x)))
