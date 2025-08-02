fib = [1,1]
sum = 0
for i in range(2,int(input())):
    f_temp = fib[i-1] + fib[i-2]
    fib.append(f_temp)
    sum+=f_temp
print(fib)
print(sum)
