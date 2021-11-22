# a = input("Enter your age")
# age = int(a)
def age(a):  #according to this program you can add some else if function into this fucntion. In this program we define two different things 1.A function named "age" 2. A variable named "a".
    if a < 18:
        print("You are under 18")
    elif a == 18:
        print("You are 18")
    elif a > 75:
        print("You are above 75")
    elif a > 18:
        print("You are above 18 and below 75")    
    else:
        print("Enter correct age")


#We created a variable "num" to store age of the User and after that we converted it as an integer by conversion method into variable "x".


num = input("Enter your age")
x = int(num)
age(x) # Now we entered our defined function and put a variable in that function. If the value in "x" matches as per the consitions of If and Elif and Else clause it will print the data whatever user put into that clause.