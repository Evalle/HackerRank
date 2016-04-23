'''
You are given a string SS. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
'''
usin = raw_input()
l = list()
for i in usin:
    if i == i.upper():
        l.append(i.lower())
    elif i == i.lower():
        l.append(i.upper())
print ''.join(l)
