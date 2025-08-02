import string
import random
for _ in  range(int(input())):
    x = list(map(str,input()))
    new_string = ""
    unique_letters = []
    letters = string.ascii_lowercase
    for char in letters:
        if char not in set(x):
            unique_letters.append(char)
    random_char = random.choice(unique_letters)
    for char in x:
        if new_string and random_char not in new_string:
            if char == new_string[-1]:
                new_string+=random_char
        new_string+=char
    if len(x) == 1 or random_char not in new_string  or new_string == ''.join(x):
        print(new_string+random_char)
    else:
        print(new_string)

#  Solution for https://codeforces.com/contest/1997/problem/A
