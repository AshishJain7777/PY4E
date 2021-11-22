# this program is for ticket price according to distance

x = input("Enter your age for travel ticket:")
age = int(x)
h = input("Enter your total distance in Kilometers:")
distance = float(h)
charge_adult = 2.20
charge_minor = 1.60
if age > 18:
    print(distance * charge_adult)
else:
    print(distance * charge_minor)
