namelist = list()
gradelist = list()

counter = int(input())
for i in range(counter):
    name = namelist.append(input())
    grade = gradelist.append(input())

studentlist = [list(l) for l in zip(namelist,gradelist)]
print(studentlist)

