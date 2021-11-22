fhand = open('calculator_py.txt')
for line in fhand:
    if line.startswith('def'): # here pre-defined function will search the given criteria in the string or in the file we set up to read and print that line which begins with given criteria
        print(line)