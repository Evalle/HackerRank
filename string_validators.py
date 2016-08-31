'''
Task

You are given a string SS. 
Your task is to find out if the string SS contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string SS.

Constraints

0<len(S)<10000<len(S)<1000

Output Format
In the first line, print True if SS has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if SS has any alphabetical characters. Otherwise, print False. 
In the third line, print True if SS has any digits. Otherwise, print False. 
In the fourth line, print True if SS has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if SS has any uppercase characters. Otherwise, print False.

Sample Input

qA2

Sample Output
True
True
True
True
True
'''

string = input()

print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))
