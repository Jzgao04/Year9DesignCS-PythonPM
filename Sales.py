dblSales = []
dblTotal = 0.0
for i in range(0,7):
    dblX = float(input("Enter the sale amount "))
    dblSales.append(dblX)
    dblTotal = dblTotal + dblX
print("Total Sales", dblTotal)
for j in range(0,7):
      print(dblSales[j])