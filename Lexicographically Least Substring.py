string = "Apple"


def smallest_alphabet(a, n): 
    min = 'z'; 
    for i in range (n - 1):  
        if (a[i] < min): 
            min = a[i]  
    return min 



