fhand = open('calculator_py.txt')
for line in fhand:
    line = line.rstrip() # this will kill the whitespace at the end of the statement, so we will be able to see the text without new lines creating between them. 
    if line.startswith('def'):
        print(line)


# below will show the same use but with the diffrent approach.


fhand = open('calculator_py.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('def'):
        continue # it is the same operation permorming but in this we did it with the help of continue.
    print(line)