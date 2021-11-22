# as we learn that input helps us to enter out value but if we enter a numerical it will consider it as a string not a digit.
# so we have to convert it first to use as a string

euf = input("enter the floor number according to europe")
#usf = euf + 1 # this is not going to add because euf is a string value so we have do is something like following example:-
usf = int(euf) + 1
print("Usa floor plan will be",usf) 