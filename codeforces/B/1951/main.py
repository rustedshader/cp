# number cant go beyond index of number which is greater than him
# if number is after the number which is greater than him then he will try to swap with index less than greater number index which 
# has the least index among them 

for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    k -= 1
    arr = list(map(int, input().split(" ")))
    number_to_find = arr[k]
    greater_num_arr = []
    count = 0 

    for index,num in enumerate(arr):
        if num >= number_to_find and index <= k:
            greater_num_arr.append(index)

    if greater_num_arr:
        if min(greater_num_arr)-min(0,min(greater_num_arr)) >= k - min(greater_num_arr) + 1:
            arr[min(0,min(greater_num_arr))] , arr[k] = arr[k] , arr[min(0,min(greater_num_arr))]
        else:
            arr[min(greater_num_arr)] , arr[k] = arr[k] , arr[min(greater_num_arr)]

    i=0
    while True:
        if i < n - 1:
            if arr[i] > arr[i + 1]:
                if arr[i] == number_to_find:
                    count += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                if arr[i + 1] == number_to_find:
                    count += 1
        else:
            break
        i += 1
    print(count)

    



