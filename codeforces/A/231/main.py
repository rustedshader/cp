n = int(input())
line_values = []
number_values = []

for _ in range(n):
    line = input()
    line_values.append(line)

for line in line_values:
    x = line.replace(" ", "")
    y = len(x)
    no_of_ones = x.count('1')
    if no_of_ones >= 2:
        number_values.append(no_of_ones)
print(len(number_values))

# Answer for problem https://codeforces.com/contest/231/problem/A
