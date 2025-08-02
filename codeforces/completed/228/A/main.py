x = input()
input_array = x.split()
duplicates = []
for items in input_array:
    if input_array.count(items) and items not in duplicates:
        duplicates.append(items)


print(len(input_array) - len(duplicates))
# Solution for problem https://codeforces.com/problemset/problem/228/A
