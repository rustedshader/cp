arr = [100,190,134141,1414314,14,1,4,141,14,-10000,100,-220]

sum = 0
best = 0
sum_2 = 0
for i in range(0,len(arr)):
    sum = max(arr[i],sum+arr[i])
    sum_2 += arr[i]
    best = max(best,sum)

print(sum,sum_2,best)
