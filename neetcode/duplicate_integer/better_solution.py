num = [1, 2, 3, 3]
hashset = set()
for n in num:
    if n in hashset:
        print(True)
        quit()
    hashset.add(n)
print(False)
