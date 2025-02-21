def isMontonic(arr: list):
    isDecreasing = True
    isIncreasing = True

    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            isDecreasing = False
        if arr[i] > arr[i-1]:
            isIncreasing = False
    return isIncreasing or isDecreasing


a = [1,2,3,4]
print(isMontonic(a))
b = [5,5,5,5]
print(isMontonic(b))
c = [1,4,3,5]
print(isMontonic(c))
