intTotal = 0

for i in range(0,10):
    
    x = int(input())
    intTotal = intTotal + x
    
print("Average", (intTotal/10))


intNum = int(input())
intFact = 0 
for i in range(1, intNum + 1):
    if intNum % i == 0:
        intFact = intFact + 1
print(intFact)