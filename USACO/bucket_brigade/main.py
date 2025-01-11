import sys
x = sys.stdin.read()
brigade_row = 0
brigade_column = 0
rock_row = 0
rock_column = 0
lake_row = 0
lake_column = 0
for line_index,lines in enumerate(x.splitlines()):
    for index,char in enumerate(lines):
        if char == "B":
            brigade_row = line_index + 1
            brigade_column = index + 1
        if char == "R":
            rock_row = line_index + 1
            rock_column = index+1
        if char == "L":
            lake_row = line_index +1
            lake_column = index+1

initial_value = abs(brigade_row-lake_row) + abs(brigade_column-lake_column)-1

if brigade_row == rock_row == lake_row and brigade_row < rock_row < lake_row or lake_row < rock_row < brigade_row:
    initial_value+=2
elif brigade_column == rock_column == lake_column and brigade_column < rock_column < lake_column or lake_column < rock_column < brigade_column:
    initial_value+=2

print(initial_value)
