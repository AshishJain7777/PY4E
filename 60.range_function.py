print(range(4))
friends = ["ashish" , "kumar" ,"jain"]
print(len(friends))
print(range(len(friends)))

for friend in friends: # this loop is the basic loop as we use before
    print("happy new year:",friend)
for i in range(len(friends)): # this loop will focus on the position of the word because we added a function called range which begins its work from the given len function which holds the place of the string in a variable.
    friend = friends[i]
    print("happy new year:",friend.upper())