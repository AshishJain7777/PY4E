data = "From ashish.jain@gmail.com Sat Jan 5 09:14:16 2008"
atpos = data.find("@") # atpos"= @ poistion"
# as per data we find @ sign in the string.
print(atpos) # we get the poisition of the sign we were finding and we stored it.

sppos = data.find(" ",atpos) # here we find the space which is typed in first and where to begin has been put in the last of the bracket.
print(sppos) # we stored it's value too.

host = data[atpos+1 : sppos] #We stored all the data we generated in a variable .here we dont want the @ sign we go for a step further and take that value into account. And we put together both of the value anf we get to know the domian name.
print(host)


text = "X-DSPAM-Confidence:    0.8475"
num = text.find(" ")
num = float(num)
num2 = text.find("5",num)
num2 = float(num2)
tot = text[num+1 : num2]
print(tot)