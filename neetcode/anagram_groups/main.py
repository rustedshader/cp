strs = ["act","pots","tops","cat","stop","hat","tac"]
res = {}

for items in strs:
    if ''.join(sorted(items)) not in  res:
        res[''.join(sorted(items))] = ""
    res[''.join(sorted(items))] += items + " "

y=[]
for items in  res.values():
   y.append([x for x in items[:-1].split(" ")])

print(y)
