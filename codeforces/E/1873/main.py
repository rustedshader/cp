for _ in range(int(input())):
    n,max_wat = map(int,input().split(" "))
    n_arr =list(map(int,input().split(" ")))
    # n -> no of columns
    # max_wat -> max amount of water
    # n_arr -> height of the corals
    max_height = max_wat + sum(n_arr)

    print(max_height)
