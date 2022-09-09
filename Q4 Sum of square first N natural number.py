'''a recursive python function to calculate 
sum of square first N natural numbers.'''

def f(n):
    if n==1:
        return 1
        
    return (n*n)+f(n-1)
r=f(int(input("Enter a number")))
print("Sum of square first n natural no=",r)
    