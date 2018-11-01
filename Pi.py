import math

intN = int(input())

pi = float(0.0)

for i in range(0, intN+1):
    pi = pi + math.pow(-1,i) *(1/ (2*i + 1)):
    
print(pi*4)