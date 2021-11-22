fhand = open('calculator_py.txt')
count = 0 # we created a variable with value zero, in which we later add some value.
for line in fhand: # line is using to store the file to read it.
    count = count + 1 # the reading is going to be sequencly so as per line count will grow gradually.
print("line count:",count) # at last when the for loop will ended count stored some increased value. Now it will show.