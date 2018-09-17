print("- Slope Calculator -")
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
