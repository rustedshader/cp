s = "ab"
t = "a"

char_set = {}

for char in s:
    x = s.count(char)
    char_set.update({char:x})

p = []

for k,i in char_set.items():
    if k in t and t.count(k) == i:
        p.append(k)

print(p)
print(set(s))
if len(p) == len(set(t)) == len(set(s)):
    print(True)
else:
    print(False)

#My code so bad i want to vomit on it !!!
