a = -10
b = 55
c = -4
d = 4
e = 34

smallest = None # None is used to assign no value, it is used just to create empty variable.
print("before")
for value in [a,b,c,d,e]:
    if smallest is None:  # "is" Is stonger than "=" sign. It is also used to check the equality of the number.
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print("after", smallest)


# "is" is stronger than == sign, according to python if we check (0 == 0.0 , python will say yes and statement will be true)
# But if we use ( 0 is 0.0 , the statement goes false because both value aren't the same, one is of integer value and other is consist of float value)
# "is" stands for "is the same as"
# Only use "is" when you want some serious equation otherwise, choose ==. If you opt for "is" it will create complexity to understand for python as well as you.
# Use "is" only, when you use variable value "None" or when you ask python for true false.