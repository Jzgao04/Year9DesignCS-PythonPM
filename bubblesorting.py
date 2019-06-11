def bubbleSort(arr): 
    n = len(arr) 
  

    for i in range(n): 
  

        for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)


arr = [9, 1, 2, 6, 4, 7] 
  
bubbleSort(arr) 
  

