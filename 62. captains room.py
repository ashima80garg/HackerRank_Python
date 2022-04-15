import collections
k=int(input())
rooms=list(map(int,input().split()))
family_grps=k+1
d=dict(collections.Counter(rooms))
for key,v in d.items():
    if(v!=k):
       print(key) 