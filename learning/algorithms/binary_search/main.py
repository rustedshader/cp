arr = [1,9,12,14,18]

a = 0
b = len(arr)-1



while (a<=b):
    k = int((a+b)/2)
    if(arr[k] == 14):
        print("14 found !",k)
    if arr[k] > 14:
        b = k-1
    else:
        a=k+1
