input_numbers = input()
n = int(input_numbers.split(" ")[0])
m = int(input_numbers.split(" ")[1])

numbers_possible = []

bigger_number = max(n,m)


for i in range(0,bigger_number+1):
    if i*i <= bigger_number:
        for z in range(0,bigger_number+1):
            if i*i + z == n and z*z + i == m:
                # print("i",i,"z",z)
                numbers_possible.append("Possible")

print(len(numbers_possible))
# Answer for problem https://codeforces.com/problemset/problem/214/A
