'''
Task 
You are given an integer, NN, on a single line. The next line contains NN space-separated integers. Create a tuple, TT, of those NN integers, then compute and print the result of hash(TT).

Note: hash() is one of the functions in the __builtins__ module.

Input Format

The first line contains an integer, NN (the number of elements in the tuple). 
The second line contains NN space-separated integers describing TT.

Output Format

Print the result of hash(TT).

Sample Input

2
1 2
Sample Output

3713081631934410656
'''
print hash(tuple(map(int, raw_input().split(' '))))

# or 

n = int(raw_input())
l = list()
integers = raw_input().split()
for i in integers:
        l.append(int(i))
print hash(tuple(l))

