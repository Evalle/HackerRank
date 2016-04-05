''' Task 
Initialize your list (L = []) and follow the NN commands given over NN lines.

Each command will be 11 of the 88 commands given above. The extend(LL) method will not be used. Each command will have its own value(s) separated by a space.

Input Format

The first line contains an integer, NN (the number of commands). 
The NN subsequent lines each contain one of the 88 commands described above.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
''' 
counter = input()
l = list()
while counter > 0:
    command = raw_input().split(" ")
    if 'insert' in command:
        l.insert(int(command[1]), int(command[2]))
    if 'print' in command:
        print l
    if 'remove' in command:
        l.remove(int(command[1]))
    if 'append' in command:
        l.append(int(command[1]))
    if 'sort' in command:
        l.sort()
    if 'pop' in command:
        l.pop()
    if 'reverse' in command:
        l.reverse()
    if 'count' in command:
        l.count(int(command[1]))
    if 'index' in command:
        l.index(int(command[1]))
    counter -=1
# also it can be a good idea to have 'for i in xrange(counter)' so you don't need to use counter anymore
