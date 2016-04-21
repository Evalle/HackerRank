'''
# Python program to display the Fibonacci sequence up to n-th term using recursive functions
'''
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

nterms = int(input("How many terms? "))

if nterms < 1:
    print("Please enter a positive number")
else:
    for i in range(nterms):
        print(fib(i))
