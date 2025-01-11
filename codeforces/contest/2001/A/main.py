x = """7
1
1
3
1 2 3
3
1 2 2
5
5 4 3 2 1
6
1 1 2 2 3 3
8
8 7 6 3 8 7 6 3
6
1 1 4 5 1 4"""

lines = x.splitlines()
t = int(lines[0])

for i in range(1,len(lines),2):
    char = lines[i+1].split(" ")
    char = [int(t) for t in char]
    char.sort()
    count = 0
    while len(set(char)) != 1:
        for k in range(0,len(char)):
            if k<len(char)-1:
                if char[k] > char[k-1] and char[k] != char[k-1]:
                    print(char[k],char[k-1])
                    char.remove(char[k])
                    print(char)
                    print(set(char))
                    count+=1
                    break
                if char[k] < char[k+1] and char[k] != char[k+1]:
                    print(char[k],char[k+1])
                    char.remove(char[k])
                    print(char)
                    print(set(char))
                    count+=1
                    break
    print("Answer is",count)
