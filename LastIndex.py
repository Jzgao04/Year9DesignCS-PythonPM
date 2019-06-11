str = input()

def findLastIndex(str, x): 
  

    for i in range(len(str) - 1, -1,-1): 
        if (str[i] == x): 
            return i 
  
    return -1
  
x = '1'
index = findLastIndex(str, x) 
  
if (index == -1): 
    print("-1") 
else: 
    print(index) 
  