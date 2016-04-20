'''
Write a recursive Python function to print the factorial of a number n (ie, returns n!).
'''
usersn = int(input())
def fact(n):
    if n < 0:
        return "number should be positive"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(usersn))
