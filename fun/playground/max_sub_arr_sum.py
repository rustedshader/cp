array = [-1,2,4,-3,5,2,-5,2]
best = 0
sum = 0
for k in range(0,len(array)):
    sum = max(array[k],sum+array[k])
    best = max(best,sum)
    # print(k,"Sum",sum,"Best",best)

print(best)
