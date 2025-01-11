x = """10 7
hello my name is Bessie and this is my essay"""

lines = x.splitlines()
arr = lines[1].split()
print(arr)
temp = 0
inital_string = ""
for index,char in enumerate(arr):
    if len(char) + temp > 7:
        print(inital_string)
        temp = 0
        inital_string = ""
    if len(char) + temp < 7 and index+1 == len(arr):
        print(char)
    inital_string += char + " "
    temp+=len(char)
