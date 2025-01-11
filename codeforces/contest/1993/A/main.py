import sys
# Time: 124 ms	Memory: 3600 KB
x = sys.stdin.read()
lines = x.splitlines()
t = int(lines[0])
for i in range(1,t*2+1,2):
    no_of_pairs = int(lines[i])
    string = lines[i+1].replace('?','')
    sum = 0
    if string:
        char_dic = {}
        for char in string:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1
        for char_count in char_dic.values():
            sum += min(char_count, no_of_pairs)
        print(sum)
    else:
        print(0)


# First attempt of answer Time: 124 ms	Memory:3300 KB
# import sys

# x = sys.stdin.read()
# lines = x.splitlines()
# t = int(lines[0])
# for i in range(1,t*2+1,2):
#     no_of_pairs = int(lines[i])
#     string = lines[i+1].replace('?','')
#     sum = 0
#     if string:
#         for char in set(string):
#             sum += min(string.count(char), no_of_pairs)
#         print(sum)
#     else:
#         print(0)

# Answer for https://codeforces.com/contest/1993/problem/A
