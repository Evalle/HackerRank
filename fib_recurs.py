'''
The Fibonacci numbers are the numbers of the following sequence of integer values: 

    0,1,1,2,3,5,8,13,21,34,55,89, ... 
'''
usersinput = int(input())
def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(usersinput))
