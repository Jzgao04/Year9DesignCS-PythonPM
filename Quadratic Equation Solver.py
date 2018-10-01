

'''
Read three integer input from the user represents the coefficients of a quadratic equation and use the qudratic formula to calculate the roots
Enter the Coefficient of X^2 : 1
Enter the Coefficient of X :   6
Enter the Coefficient of Constant : 8
The first root is : -2.0
The second root is : -4.0
'''

import math
a = int(input("Enter the X^2 Coefficient:"))
b = int(input("Enter the X Coefficient:"))
c = int(input("Enter the constant term:"))
root1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c)) / (2 * a)
root2 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c)) / (2 * a)
print("The first root is ", root1)
print("The second root is ", root2)