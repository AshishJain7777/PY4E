a = 32
b = 21
c = 97
d = 11
e = 19
f = 2
g = 100

print("Before")
for value in [a,b,c,d,e,f,g]:
    if value > 20:  # by the help of loop if the value turns more than 20 so, it will print that value, if not it will go for another variable to check. When the variables end the program will end with a message "all done"
        print("This is greater",value)
print("all done")