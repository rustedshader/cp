# 4 -> no of test cases
# 1 -> length of array a aka n
# 6 -> item of array a
# 3 -> length of array b
# 1 3 2 -> item of array b
# 5 -> length of array c
# 4 7 4 2 9 -> items of array c
# 7 -> length of array d
# 3 1 4 1 5 9 2 -> items of array d

problem_input = """4
1
6
3
1 3 2
5
4 7 4 2 9
7
3 1 4 1 5 9 2"""

m = {}
no_of_problems = int(problem_input.splitlines()[0])

for i in range(2,no_of_problems*2+1,2):
    x = (problem_input.splitlines()[i]).split(" ")
    while len(x) >= 2:
        m.update({x.pop(1):x.pop(-1)})

print(m)


    # numbers = problem_input.splitlines()[i].split(" ")
