a = 2
b = 44
c = 12
d = 24
e = 100
f = 12
g = 123
print("before")
for thing in [a,b,c,d,e,f,g]:
    print(thing)
print("after")
#
#
#
largest_so_far = -1  # we assigned a number to this variable
print("before",largest_so_far )  
for the_num in [a,b,c,d,e,f,g]:  # here we created for loop in which the variables values is going to store in "the_num" variable
    if the_num > largest_so_far: # if the stored value in the_num which comes from for loop is is bigger than largest_so_far so it will go down and evaluate.
        largest_so_far = the_num # if the condition is true this will happen otherwise it will skip this part every time and reach the part which is below.
    print(largest_so_far,the_num) # this part will always run throughout the loop no matter what happen, because of indentation.
print("after",largest_so_far) # when the loop completed this last statement will apperar with the last greatest or bigger value.


a = 220
b = 123
c = 11
d = 33
e = 9
f = 2
g = 0

print("before")
for thing in [a,b,c,d]:
    print(thing)
print("after")
#
#
#
small_so_far = 100
print("before",small_so_far )
for the_num in [a,b,c,d,e,f,g]:
    if the_num < small_so_far: # this is for the smallest so far.
        small_so_far = the_num
    print(small_so_far,the_num)
print("after",small_so_far)


