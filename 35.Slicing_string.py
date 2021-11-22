s = "monty python" # We store a string in a variable.
print(s[0:4]) # now we are recalling the string and priting, but the value in bracket shows starting and end point. But starting point show the exact poisition of the string but the last value does not land us to last number it will show the value before that.
print(s[6:7]) # Start from 6 but not include 7.
print(s[6:20]) # it will show till the 19 because 20 is not included, but it is not a good practice. It won't throw error but choose values wisely.

# some errorfull programming.

print(s[:2]) # this will start automatically or we can say it is default it will start from the beginning and end before 2.
print(s[8:]) # same goes for him but in this it will start from poistion 8 and end till the string ended
print(s[:]) # this is very bad practice it will show or print the whole string.