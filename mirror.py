'''
Write a program to find the mirror image of a binary tree? 

if a tree is like 

01 
02 03 
04 05 06 07 

The mirror will be like 

01 
03 02 
07 06 05 04
'''
counter = int(raw_input())
l = list()
while counter > 0:
    line = raw_input().split()
    line.reverse()
    l.append(line)
    counter -=1
for list in l:
    print ' '.join(list)
