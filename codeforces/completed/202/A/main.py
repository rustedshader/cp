import string
input_string = input()

char_dictionary = {}

for char in input_string:
    index = string.ascii_lowercase.index(char) + 1
    char_dictionary.update({char: index})

largest_index = max(char_dictionary.values())

selected_char  = ""

for char,key in char_dictionary.items():
    if key == largest_index:
        selected_char = char

final_otuput= selected_char * input_string.count(selected_char)
print(final_otuput)

# Just print largest character and all its occurece as one string !
# Solved https://codeforces.com/problemset/problem/202/A
