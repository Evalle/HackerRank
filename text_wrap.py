'''
Task

You are given a string  and width . 
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, . 
The second line contains the width, .

Output Format

Print the text wrapped paragraph.

Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output

 ABCD
 EFGH
 IJKL
 IMNO
 QRST
 UVWX
 YZ 
 '''

import textwrap

string = input()
number = int(input())
print(textwrap.fill(string, number))
