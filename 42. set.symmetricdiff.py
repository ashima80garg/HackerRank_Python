n=int(input())
l1=list(map(int,input().split()))
set1=set(l1)
m=int(input())
l2=list(map(int,input().split()))
set2=set(l2)
union=set1|set2
intersection=set1&set2
print(len(union-intersection))