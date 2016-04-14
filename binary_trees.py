counter = int(raw_input())
while counter > 0:
    line = raw_input().split()
    line.reverse()
    newl = map(int, line)
    counter -= 1
for i in newl:
    print i,
