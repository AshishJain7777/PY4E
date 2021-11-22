## this is the program to increase the pre exisiting variable valur by the help of for loop.

a = 34
b = 234
c = 23
d = 24


zork = 0
print("before",zork)
for thing in [a,b,c,d]:
    zork = zork + 1  # we use + 1 as a expression to increase the zork value continiously but it will on increase gradually till the all variables are not tested or printed or evaluated.
    # each time the zork value get changed by adding '1'
    print(zork,thing)
print("After",zork)


a = 34
b = 234
c = 23
d = 24


zork = 0
print("before",zork)
for thing in [a,b,c,d]:
    zork = zork + thing # we used the same method as we used above but this time we added the variable which holds our extra variables value, and added to the pre-exisitng variable zork. means if zork is 0 and we added a which is 34 so the value of zork changes to 34 and so on with other variables. 
    print(zork,thing)
print("After",zork)
