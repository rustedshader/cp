db_2 = {}
for _ in range(int(input())):
    s = input()
    if s not in db_2:
        db_2[s] = 0
        print("OK")
    else:
        db_2[s] += 1
        print(f'{s}{db_2[s]}')