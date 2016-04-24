'''
Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, SS. 
The next line contains an integer ii, denoting the index location and a character cc separated by a space.

Output Format 
Using any of the methods explained above, replace the character at index ii with character cc.

Sample Input

abracadabra
5 k
Sample Output

abrackdabra
'''
line = list(raw_input())
options = raw_input().split()
line[int(options[0])] = options[1]
string = ''.join(line)
print string
