'''
input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

1≤len(string)≤2001≤len(string)≤200 
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output
2
'''
haystack = raw_input()
needle = raw_input()
count = 0
for i in range(0,len(haystack)-len(needle)+1):
    if needle == haystack[i:i+len(needle)]:
        count += 1    
print count
