import sys
x = sys.stdin.read()
lines = x.splitlines()
t = int(lines[0])
for i in range(1,t*3+1,3):
    a = lines[i+1].split(" ")
    a = [int(nums) for nums in a]
    b = lines[i+2].split(" ")
    b = [int(nums) for nums in b]
    min_a = min(a)
    min_b = min(b)
    count = 0
    for a_num, b_num in zip(a, b):
            diff_a = a_num - min_a
            diff_b = b_num - min_b
            count += max(diff_a, diff_b)
    print(count)
