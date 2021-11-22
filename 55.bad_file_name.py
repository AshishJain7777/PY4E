fname = input("Enter the file name")
count = 0
try:
    fhand= open(fname)
except:
    print("'",fname,"'""This file Does not exist")
    quit()
for line in fhand:
    if line.startswith('def'):
        count =  count + 1
print("there were",count,"define functions lines in",fname)
# in this program if user find some inappropriate file or files that does not exist, so it will throw an error and shuts the program. We can create or re-design this program until the write file isn't executed through the help of "loops"