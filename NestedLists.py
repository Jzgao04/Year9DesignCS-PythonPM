#Nested List

intMagic = [[1,2,3], [4,5,6], [7,8,9]]
#Reading input for intMagic using a loop


#Printing the Nested List using Nested for loop
'''
1 2 3
4 5 6
7 8 9
'''

for i in range(0, len(intMagic)):
    for j in range(0, len(intMagic[i])):
        print intMagic[i][j], "\t",
    print("\n")
    
for i in intMagic:
    for j in i:
        print j , "\t",
    print("\n")
    
# Finding the sum of the rows in intMagic
intRowSum = [] # let store each sum of each row into a list

for i in range(0, 3):
    row = 0
    for j in range(0, 3):
        row = row + intMagic[i][j]
    intRowSum.append(row)
print(intRowSum)

#Calculate and print the col sum

intRowSum = []
intColSum = []
for i in range(0,3):
    row = 0
    col = 0
    for j in range(0,3):
        row = row + intMagic[i][j]
        col = col + intMagic[j][i]
    intRowSum.append(row)
    intColSum.append(