from collections import Counter
n=int(input())
l1=[]
for i in range(n):
    arr=input()
    l1.append(arr)
print(len(set(l1)))
d=dict(Counter(l1))
for key,values in d.items():
    print(values,end=" ")
