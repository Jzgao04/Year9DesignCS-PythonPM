print("Welcome To Python")
print("\"Welcome To Python\"")
print("\\")
print("FirstName\tLastName")
print("Welcome\nTo\nPython")
print("Bonjour, tout le monde!")
#print("Welcome", "To", "Python", sep = "/n")

print("////\\\\\\\\")
print("\\\\\\\\////")

print("B\tI\tN\tG\tO")
print("2\t20\t42\t60\t64")
print("14\t25\t32\t55\t70")
print("5\t18\tFREE\t53\t67")
print("12\t16\t31\t46\t75")
print("10\t22\t39\t59\t71")

#Input
y2 = int(input("What is Y2?"))
y1 = int(input("What is Y1?"))
x2 = int(input("What is X2?"))
x1 = int(input("What is X1?"))
print("Your first point is:", (x1, y1))
print("Your second point is:", (x2, y2))
slope = float(y2 - y1) / (x2 - x1)
#Process
print("Your Slope is: ", slope)