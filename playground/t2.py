import re 
    
def occurrences(string, sub):
    res = []
    ind = 0
    while ind < len(string) - len(sub) + 1:
        found = string.find(sub, ind)
        #print("ind = {} found = {}".format(ind, found))
        if found != -1:
            res.append(found)
            ind = found + 1
        else:
            break
    return res


for _ in range(int(input())):
    R,C = map(int,input().split(" "))
    G = []
    for _ in range(R):
        G.append(input())
    r,c = map(int,input().split(" "))
    P = []
    for _ in range(r):
        P.append(input())
    string1 = "\n".join(G)
    string2 = "\n".join(P)
    print()
    print(string1)
    print()
    print(string2)
    print()
    print(occurrences(string1,string2))
