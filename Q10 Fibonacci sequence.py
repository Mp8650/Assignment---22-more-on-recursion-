'''A recursive python function to find the 
pNth term of the Fibonacci series.'''

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
num=int(input(" How many term you want to print ="))
if num<=0:
    print("Enter a positive number")
else:
    print("fibanacci sequence")
    for i in range (num):
        print (fib(i),end=' ')
        