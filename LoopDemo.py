#Loop Demo
for i in range(0, 6, 1):
	print(i)

#How would the above loop run 
#We would reach line 27
# i = 0, 0 < 6, True RUN Loop
# i = 1, 1 < 6, True RUN Loop
# i = 2, 2 < 6, True RUN Loop
# i = 3, 3 < 6, True RUN Loop
# i = 4, 4 < 6, True RUN Loop
# i = 5, 5 < 6, True RUN Loop
# i = 6, 6 < 6, FALSE EXIT

print("***********************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)
print("***********************")
print("Write a loop that will print out even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)
for i in range(3, 0, -1):
	print(i)
print("***********************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101, -1, -1):
	print(i)

#BEST PRACTICE: NEVER TYPE IN LENGTH OF STRING AS A NUMBER. ALWAYS HAVE THE COMPUTER FIND IT.

s = "Fish_food"
for i in range(0,len(s),1):
	print(s[i])

for i in range(len(s) - 1, -1, -1):
	print(s[i])
