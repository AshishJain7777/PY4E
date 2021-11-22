fhand = open('calculator_py.txt')
for line in fhand:
    line = line.rstrip()
    if not 'def' in line: # same function as previous but with different approach.
        continue
    print(line)

    # in this we didn't use startswith , conversely we defined that we need this string to be found in the given document.