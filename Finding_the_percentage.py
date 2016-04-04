# Enter your code here. Read input from STDIN. Print output to STDOUT
students = {}
nofstud = int(input())
while nofstud > 0:
    info = raw_input().split(" ")
    students[info[0]] = [info[1],info[2],info[3]]
    nofstud -= 1
question = raw_input()
if (question in students):
    res = (students[question])
    sum = 0
    for i in res:
        sum += float(i)
    print ('{:.2f}'.format(sum / 3))
else:
    print 'There is no student with name: ', question
