# file1 = open('new_file.txt','w')
# file1.write('This is a new file created by the help of Python')
# file1.close()
file2 = open('simple.txt','r')
for i in file2:
    print(i)


# open function is used to open an readable file , by the use of given syntax.
#open("filename","mode") 
#there are 4 types of mode:-
#"r" = reading
#"w" = writing
#"a" = appending
#"r+" = reading and writing