'''A recursive python function to print 
binary of a given decimal number.'''

def f(n):
    if n>0:
        rem=n%2
        f(n//2)
        print(rem,end='')
f(int(input("Enter a decimal number =")))

    