import sys

x = sys.stdin.read()
no_of_orange_juice = x.splitlines()[0]

volume_fraction_of_orange_juice_percentage = x.splitlines()[1].split(" ")
# volume_fraction_of_orange_juice_fraction = []
sum = 0
for nums in volume_fraction_of_orange_juice_percentage:
    sum += int(nums)/100
# print(sum)
print(sum/int(no_of_orange_juice)*100)

# print(no_of_orange_juice)
