from itertools import combinations
arr= input().split()
word,n=arr[0],int(arr[1])
a=sorted(word)
for i in range(n):
    ans=combinations(a,i+1)
    for i in ans:
        print(''.join(i))
    