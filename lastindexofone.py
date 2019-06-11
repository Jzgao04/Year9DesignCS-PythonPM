str = input()

def findLastIndex(str, x): 
    index = -1
    for i in range(0, len(str)): 
        if str[i] == x: 
            index = i 
    return index 

x = '1'
  
index = findLastIndex(str, x) 
  
if index == -1: 
    print("-1") 
else: 
    print(index) 
  