n=int(input())
arr1=list(map(int,input().split()))
set1=set(arr1)
m=int(input())
arr2=list(map(int,input().split()))
set2=set(arr2)
result_set1=set1-set2
result_set2=set2-set1
final_result=result_set1|result_set2
result_list=list(final_result)
result_list.sort()
for i in result_list:
    print(i)
    