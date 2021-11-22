def addtwo(a, b): # we created two variable in it.
    added = a + b # we created a variable and stored the addition of both pre-created variable
    return added # now added is ready to return the value. Whenever it is called by function.

one = input("enter first value to add")
second = input("enter second value to add")
a = int(one)
b = int(second)

x = addtwo(a, b) #Now "addtwo" function is created to add two values and it will return the answer of the equation in new created variable "x"
print(x) # "x" have the sum of the two numbers.



