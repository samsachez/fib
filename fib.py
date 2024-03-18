nterms =int(input("please enter the number of terms :"))
n1, n2 , = 0, 1
n3 = 0

print("fibonacci_series :{}, {}," .format(n1, n2), end=" ")
for i in range (0, nterms - 2) :
    n3 = n1 + n2
    print ("{}," .format(n3))
    n1 = n2
    n2 = n3

      

 
    
    
    

    
    