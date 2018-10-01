import math
print("Enter the height less than 4.5")
dblTime = float(input("Enter The Time"))
dblHeight = 100 - 4.9 * math.pow(dblTime,2)
print("The height of the object is:")
print(dblHeight)

#Pizza Cost
intDiameter = int(input("Enter the diameter of the pizza:"))
dblCost = 0.05 * math.pow(intDiameter,2) + 0.75

#Change calculator
intCents = int(input("Enter the change in Cents "))
intQuarters = intCents // 25 
intDimes = (intCents % 25) / 10
intNickel = ((intCents % 25) % 10) // 5
intPennies = (intCents % 25 ) % 10 % 5
print("Quarters ","\t", intQuarters)
print("Dimes ","\t", intDimes)
print("Nickels ","\t", intNickel)
print("Pennies ","\t", intPennies)