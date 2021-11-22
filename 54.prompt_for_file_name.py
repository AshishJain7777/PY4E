fname = input("Enter the file name")
fhand= open(fname)
count = 0
for line in fhand:
    if line.startswith('def'):
        count =  count + 1
print("there were",count,"define functions lines in",fname)

# this program will calculate the line we want to search , with the help of startswith.