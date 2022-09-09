''' a recursive python function to calculate 
the factorial of a number.'''

def f(n):
    if n==1:
        return 1
        
    return n*f(n-1)
r=f(int(input("Enter a number")))
print("Factorial of a number =",r)
    