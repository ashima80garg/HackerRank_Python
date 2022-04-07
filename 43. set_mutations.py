n=int(input())
l1=list(map(int,input().split()))
set1=set(l1)
m=int(input())
for i in range(m):
    cmd,n=input().split()
    l2=list(map(int,input().split()))
    set2=set(l2)
    if cmd=="intersection_update":
        set1.intersection_update(set2)
    if cmd=="update":
        set1.update(set2)
    if cmd=="symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    if cmd=="difference_update":
        set1.difference_update(set2)
print(sum(set1))