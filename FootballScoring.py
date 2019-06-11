def count(n): 
  
    # table[i] will store count of solutions for value i. 
    # Initialize all table values as 0. 
    table = [0 for i in range(n+1)] 
  
    # Base case (If given value is 0) 
    table[0] = 1
  
    for i in range(2, n+1):
        table[i] += table[i-2]
    for i in range(3, n+1): 
        table[i] += table[i-3] 
    for i in range(6, n+1): 
        table[i] += table[i-6] 
    for i in range(7, n+1): 
        table[i] += table[i-7] 
    for i in range(8, n+1): 
        table[i] += table[i-8] 

  
    return table[n] 
n = 100
print('For the point total', n, 'there are', count(n), 'ways to get this score.') 
  
