x = 32
y = 44
n = "ashish"
i = "jain"
inn = 0
# if x < y:
#     try: 
#      print(n+i)
#     except:             #this statement is work as an try condition because in this I add to strings together. So, according to Python if to string are attached it will form a line of string
#      print(x+y)
# else:
#  print("bye")    
if x < y:
    try: 
     inn = int(n)
     print(inn)   #but if this will get executed so, it will run as a exception condition or "except" because in this statement I try to convert a string into an integer value and that is totally impossble in Python. So, only except condition will run 'it means' sum of two value can be seen as an output. 
    except:
     print(x+y)
else:
 print("bye")    

astr = "bob"
try:
    print("hello")# according to this part we can see that if your try block have some sort of code that is reasonable it will work, but it will only get terminated and send to except when there is something wrong you want to do with the help of python.
    istr = int(astr)  # istr is a string and it cannot be turned into an integer so it can't be executed so, at this point python will terminate it and send it to except block. And as we can see istr is appointed here as a variable and now it can hold a value and it can be easilt executed by python.  
    print("this is done")
except:
    isss = -1
print("done",isss)


rawstr = input("Enter a number")  # according to this example:  or  
try: #if we enter a number it will go down in try condition and get converted to an integer and then it will reach if condtion (if the number you entered is above than 0 you will see 'nice work')
    ival = int(rawstr)
except: #if you try to enter some string or a value less than 0 which is not possible (it will suddenly jumped away from try block and landed into except and now a value of your will be assigned as a -1 which is less than 0 so just after than it will reach if else condition and in it if the condition is less than 0 it will send your statement to else and you'll see not a number )
    ival = -1
if ival > 0:
    print("nice work")
else:
    print("not a number")