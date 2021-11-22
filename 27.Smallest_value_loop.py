from typing import NoReturn


a = 3
b = 6
c = 9
d = 2
e = 5
f = -7


smallest_so_far = 100
print("before",smallest_so_far)
for the_num in [a,b,c,d,e,f]:
    if the_num <  smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far,the_num)
print("After",smallest_so_far) 