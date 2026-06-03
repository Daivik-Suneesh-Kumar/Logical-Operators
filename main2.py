a = 10
b = 12
c = 12

print(not(a == b))

print(not(b == c))

a = "Coding"
b = "Python"

if not (a == b):
    print("Both",a,b, "are different")

a = 4
b = 5

if not(a == b):
    print("Both", a,b,"are different")

a = (int(input("Enter your number")))
if not (a % 2 == 0):
    print(a,"is an odd number.")
