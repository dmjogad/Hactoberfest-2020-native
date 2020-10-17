def square_sum(n) : 
    total = 0
    for i in range(1, n+1) : 
        total = total + (i * i) 
      
    return total

n = 4
print(square_sum(n)) 
