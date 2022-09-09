'''A recursive python function to print 
Octal of a given decimal number.'''

def f(n):
    if n>0:
        rem=n%8
        f(n//8)
        print(rem,end='')
f(int(input("Enter a decimal number =")))

    