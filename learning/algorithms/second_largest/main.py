


largest = float('-inf')
second_largest = float('-inf')

arr = [6,6,1,2,3,4,5,6,6]


for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest  = num

print(second_largest)
