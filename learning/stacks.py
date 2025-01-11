# Last in First Out (LIFO)
# We have to pop the items and move it towards the left as we cannot leave the quue empty
# First In First Out

stk = []


stk.append(5)

stk.append(2)

x = stk.pop()

print(x)
print(stk)


# Ask if something in the stack

if stk:
    print(True)
