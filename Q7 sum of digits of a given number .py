'''a recursive python function to calculate 
sum of the digits of a given number.'''

def f(n):
    if n==0:
         return 0
    return(n%10+f(n//10))
       
s=f(int(input("Enter a number")))
print("sum of the digits of a number  =",s)
    