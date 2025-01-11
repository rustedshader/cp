for _ in range(int(input())):
    n = int(input())
    for k in range(n):
        arr = []
        for i in range(1,n+1):
            if (k%2 == 0) :
                if(i%2 != 0):
                    arr.append("##")
                else:
                    arr.append("..")
            else:
                if(i%2 != 0):
                    arr.append("..")
                else:
                    arr.append("##")
        print(''.join(arr))
        print(''.join(arr))
