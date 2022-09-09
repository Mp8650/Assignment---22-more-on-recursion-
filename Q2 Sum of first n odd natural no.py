'''a recursive python function to calculate 
sum of first N odd natural numbers.'''

def f(n):
    if n==1:
        return 1
    return (n*2-1)+f(n-1)
r=f(int(input("Enter a number")))
print("Sum of first n odd natural no=",r)
