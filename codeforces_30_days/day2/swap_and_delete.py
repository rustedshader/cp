# 1) delete one character from s cost ---> 1
# 2) swap any one pair of character in s cost ---> 0

def solve(s):
    len_s = len(s)
    zero_count = s.count("0")
    ones_count = len_s - zero_count
    _i_ = 0
    for i in range(len_s):
        if s[i] == "0" and ones_count > 0:
            ones_count -= 1
            _i_ +=1
        elif s[i] == "1" and zero_count > 0:
            zero_count -= 1
            _i_ += 1
        else:
            break
    # len_s - _i_ is characters that can't be swapped as either zero_count is zero or ones_count is zero 
    # so we subtract _i_ from length of string to get how many min characters to remove 
    return len_s - _i_

for _ in range(int(input())):
    s = input()
    print(solve(s))