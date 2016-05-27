namelist = list()
gradelist = list()
numbers = list()
newlist = list()

counter = int(input())

for i in range(counter):
    name = namelist.append(input().strip())
    grade = gradelist.append(input().strip())

studentlist = [list(l) for l in zip(namelist,gradelist)]

for list in studentlist:
     for element in list:
         if element.isdigit():
             numbers.append(int(element))

for i in numbers:
    if i not in newlist:
        newlist.append(i)
newlist.sort()
newlist.remove(max(newlist))
minimum = newlist.pop()

for list in studentlist:
     for element in list:
         if minimum in list:
             print(list)


