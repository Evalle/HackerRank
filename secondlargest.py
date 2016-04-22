'''
Input Format
The first line contains NN. The second line contains an array AA[] of NN integers each separated by a space.

Output Format
Output the value of the second largest number.
'''
nterms = int(input())
numbers = raw_input().split()
l = list()
newlist = list()
for i in numbers:
    l.append(int(i))
# creating list of unique numbers
for i in l:
    if i not in newlist:
        newlist.append(i)
newlist.sort()
newlist.remove(max(newlist))
print newlist.pop()
