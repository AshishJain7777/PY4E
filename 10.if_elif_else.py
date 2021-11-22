h = input("Enter hour")
hrs = float(h)
p = input("enter amount")
pay = float(p)
min_hrs = 40
pay_after = 15.75
if hrs > 40:
    hrs = hrs - min_hrs
    total = min_hrs * pay
    hrs = hrs * pay_after
    last = total + hrs
    print(last)
elif hrs < 40:
    total = hrs * pay
    print(total)
else:
    print("Maybe your given values are wrong , please try again")

# or a simple example is a given below
x = input("enter a value between 1-10")
xx = int(x)
if xx < 5:
    print("your value is less than 5")
elif xx > 5 & xx < 10:
    print("your value is less than 10 and more than 5")
else:
    print("please enter value between 1 to 10")

    # another example

v = input("enter a number between 1 to 100")
value = int(v)
if value < 10:
        print("less than 10")
elif value < 20:
        print("less than 20")
elif value < 40:
        print("less than 40")
elif value < 100:
        print("less than 100")
else:
        print("please enter the value between 1 - 100")


# note the questions you ask in i else like if this happens do that ( if a < 2) so try to make them more sensible, and try to put them in order to work correctley