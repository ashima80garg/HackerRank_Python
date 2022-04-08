import itertools
a = input()
x = itertools.groupby(a)
l=[]
for k,g in x:
    ans=len(list(g))
    print((ans,int(k)),end=" ")
