x = input("Enter the desired number")
y = input("Enter another number")
z = input("Enter the last number")

for loop in [x,y,z]: # this for loop store the all variable in chronological order like : first "x" second "y" last "z", and after that chronolically assigned that value to the newly created variable as example : "loop". And when the loop ends it draw himself back from loop and print the last statement.
    print(loop)
print("Here the program ends")

# we always don;t have to put our variables in a bracket we can also put them in a variable like given below:-


x = input("Enter the name")
y = input("Enter another name")
z = input("Enter the name")

friends = [x,y,z]
for friend in friends: # according to this we didn't assigned the values in for loop , we put a value holding pre-exesting variable to compute data from there.
    print("hello number",friend)
print("all done")