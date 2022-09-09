'''a recursive python function to calculate 
sum of first N natural numbers.'''

def f(n):
    if n==1:
        return 1
    return n+f(n-1)
r=f(int(input("Enter a number")))
print(r)
       
    
    