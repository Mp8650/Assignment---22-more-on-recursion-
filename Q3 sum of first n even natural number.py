'''a recursive python function to calculate 
sum of first N even natural numbers.'''

def f(n):
    if n==1:
        return 2
        
    return (n*2)+f(n-1)
r=f(int(input("Enter a number")))
print("Sum of first n even natural no=",r)
    