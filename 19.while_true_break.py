while True:  # this is a non breakable unbounded loop but there is an exception. There is a break below.
    line = input(">") # you have a variable you have to put some string, if you continiously type some other thing what needs to break loop so loop will never end.
    if line == "done": # done is the term used to end the loop if you put the value when asked "done" loop will be ended and print you finished if you entered something else , loop isn't going to end.
        break
    print(line)
print("finished")
