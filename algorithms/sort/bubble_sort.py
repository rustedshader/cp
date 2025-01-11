x = [1, 5, 3, 6, 9]
for i in range(len(x)):
    for k in range(len(x) - 1):
        if x[k] > x[k + 1]:
            x[k], x[k + 1] = x[k + 1], x[k]

print(x)
