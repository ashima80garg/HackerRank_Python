n=int(input())
l1=list(map(int,input().split()))
set1=set(l1)
m=int(input())
l2=list(map(int,input().split()))
set2=set(l2)
result_set=set1&set2
print(len(result_set))