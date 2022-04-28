import numpy
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
for i in range(a):
    print(numpy.zeros((b,c),dtype=numpy.int))
    print()
for i in range(a):
    print(numpy.ones((b,c),dtype=numpy.int))
    print()