'''
Write a iterative Python function to print the factorial of a number n (ie, returns n!).
'''
usersnumber = int(input("Enter the number: "))
def fact(number):
    result = 1
    for i in range(1,usersnumber+1):
        result *= i
    return result
if usersnumber == 0:
    print('1')
elif usersnumber < 0:
    print('Sorry factorial exists only for positive integers')
else:
    print(fact(usersnumber))
