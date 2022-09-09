'''a recursive python function to calculate 
sum of cube first N natural numbers.'''

def f(n):
    if n==1:
        return 1
        
    return (n**3)+f(n-1)
r=f(int(input("Enter a number")))
print("Sum of cube first n natural no=",r)
    