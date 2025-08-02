s = input()
s_len = len(s)
if (s_len / 20).is_integer():
    min_number_of_rows = s_len //  20  
else:
    min_number_of_rows = (s_len // 20 ) + 1
k = -1

if s_len < 20:
    ans = s_len
else:
    if (s_len / min_number_of_rows).is_integer():
        ans = s_len // min_number_of_rows
    else:
        ans = (s_len + min_number_of_rows) // min_number_of_rows
        astrics_needed = (ans * ((s_len // ans) + 1)) - s_len 
        k = min_number_of_rows -  astrics_needed


print(min_number_of_rows, ans)
count  = ans
initial = 0

for i in range(min_number_of_rows):
    if s_len < 20:
        print(s[initial:count])
    else:
        if i == k:
            count-=1
            print(s[initial:count] + "*")
            if astrics_needed > 0:
                astrics_needed-=1
                k+=1

        else:
            print(s[initial:count])
    initial = count
    count+=ans
