def bubble_sort(arr,N):
    for i in range(N):
        for k in range(N-1-i):
            if arr[k] > arr[k+1]:
               arr[k] , arr[k+1] = arr[k+1],arr[k]
    return arr

x = [5,4,3,2,1]
print(bubble_sort(x,len(x)))
