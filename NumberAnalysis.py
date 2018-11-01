intNumbers = []

for i in range(0,20):
    intX = int(input("Enter an integer"))
    
intMax = intNumbers[20]
intMin = intNumbers[0]
intTotal = 0

for i in range(0,20):
    if intNumbers[i] > intMax:
        intMax = intNumbers[i]
    if intNumbers[1] < intMin:
        intMin = intNumbers[i]
    intTotal = intTotal + intNumbers [i]
    
print("The largest :", intMax)
print("The smallest :", intMin)
print("Total :", intTotal)
print("Average :", (intTotal/20))