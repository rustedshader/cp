for _ in range(int(input())):
    n = int(input())
    x_points = []
    y_points = []
    for _ in range(n):
        x,y = map(int,input().split(" "))
        x_points.append(x)
        y_points.append(y)

    for _,index in enumerate(x_points):
        if x_points.count(_) > 2:
            print(x_points[index],y_points[index])
    print()

        # Right angle triangle cases -->
        # 1 ) middle x element between two x points and diffrenct y
        # 2 ) same x and different y of 2 points and other points with same x as these points can be right angle triangle
