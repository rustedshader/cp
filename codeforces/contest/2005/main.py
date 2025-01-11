k = ['n','a','r','e','k']
for _ in range(int(input())):
    n, m = map(int,input().split())
    f = []
    for _ in range(n):
        f+=list(input())

    print("This is f --> ",f)
    gpt = 0
    chance = 0
    m = 0
    score = 0
    index_arr = []
    f_len_const = len(f)
    f_len = len(f)
    while(f_len>0):
        found = False
        for w in k:
            if chance % 2 == 0 and f_len_const >= 5:
                if w in f:
                    found = True
                    m+=1
                    if m==5 or m==f_len_const:
                        chance+=1
                    if m ==5:
                        m=0
                        score+=5
                        f.remove('n')
                        f.remove('a')
                        f.remove('r')
                        f.remove('e')
                        f.remove('k')
                        f_len-=5
            else:
                if w in f:
                    found = True
                    gpt+=1
                    m+=1
                    f.remove(w)
                    f_len-=1
                    if m==5:
                        m=0
                        chance+=1
        if not found:
            break
    print("------------------------------")
    print("Score is",score)
    print("GPT Score is",gpt)
    print("Final Score",score-gpt)
    print("------------------------------")
