a = 22
b = 43
c = 21
d = 32
e = 56
f = 10
g = 47
h = 98


count = 0
sum = 0
print("before",count,sum)
for value in [a,b,c,d,e,f,g,h]:
    count = count + 1   # this program shows us how to find out the average of numbers.
    #count is just used to indicate the index all the numbers.
    sum = sum + value # in this value is changing again and again because of loop but it is adding in the variable sum and sum value is increasing after every loop.
    print(count,sum,value)
print("after",count,sum,sum/count) # in this sum of all numbers are divided by the index or the count of all the numbers to find out the basic average of the numbers.