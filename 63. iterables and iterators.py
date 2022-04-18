from itertools import combinations
n=int(input())
arr=input().split()
k=int(input())
count=0
ans=list(combinations(arr,k))
#print(ans)
#print(len(ans))
for i in ans:
    #print("".join(i))
    if 'a' in (i):
        count+=1
#print(count)
res=count/len(ans)
print("{0:.3f}".format(res))