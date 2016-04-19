'''
Write a Python program to print numbers from 1 to 100 except for multiples of 3 for which you should print "fuzz" instead, for multiples of 5 you should print 'buzz' instead and for multiples of both 3 and 5, you should print 'fuzzbuzz' instead.
'''
for i in xrange(1,101):
    if i % 15 == 0:
        print 'fuzzbuzz'
    elif i % 3 == 0:
        print 'fuzz'
    elif i % 5 == 0:
        print 'buzz'
    else:
        print i
