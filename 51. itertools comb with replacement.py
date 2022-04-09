from itertools import combinations_with_replacement
arr= input().split()
word,n=arr[0],int(arr[1])
a=sorted(word)
ans=combinations_with_replacement(a,n)
for i in ans:
    print(''.join(i))
    