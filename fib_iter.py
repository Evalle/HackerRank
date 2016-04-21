'''
The Fibonacci numbers are the numbers of the following sequence of integer values: 

    0,1,1,2,3,5,8,13,21,34,55,89, ... 
'''
usersinput = int(input())
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print(fib(usersinput))
