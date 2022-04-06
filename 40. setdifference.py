n=int(input())
arr1=list(map(int,input().split()))
set1=set(arr1)
m=int(input())
arr2=list(map(int,input().split()))
set2=set(arr2)
result_set=set1-set2
print(len(result_set))
