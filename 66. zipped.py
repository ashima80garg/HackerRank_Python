n,x=input().split()
n=int(n)
x=int(x)
combine=[]
zipped = []
for i in range(x):
    arr=list(map(float,input().split()))
    combine.append(arr)
#print(combine)
zipped = list(list(x) for x in zip(*combine))
#print(zipped)
for i in zipped:
    total=sum(i)
    print(total/x)