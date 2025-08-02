# print("Formula given -> a^2 + b^2 + a + b = m + n")
# print("Formula given -> a^2 + b = n")
# print("Formula given -> a + b^2 = m")

# # m = 4
# # n = 20
# print(f"m+n -> {m+n}")

Entered_Value  = input()
j = Entered_Value.split()

n = int(j[0])
m = int(j[1])


# print("This is n ->",n)
# print("This is m ->",m)

numbers_possible = []
possible_combo = []

for  i in range(0,m+n):
    if i*i < m+n:
        numbers_possible.append(i)

for x in range(0,len(numbers_possible)):
    z = (numbers_possible[x] * numbers_possible[x]) + numbers_possible[x]
    for k in range(x+1,len(numbers_possible)):
        y =  (numbers_possible[k] * numbers_possible[k])  + numbers_possible[k]
        if z+y == m+n:
            a = numbers_possible[x]
            b = numbers_possible[k]
            if a*a + b == n:
                possible_combo.append("Possible")
            elif b*b + a == m:
                possible_combo.append("Possible")
            elif a*a + b == m:
                possible_combo.append("Possible")
            elif b*b  + a == n:
                possible_combo.append("Possible")


# print("Total Pairs  Possible ->",len(possible_combo))
if( m == n ):
    print(len(possible_combo))
else:
    print(len(possible_combo))
