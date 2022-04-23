n,m=input().split()
n=int(n)
m=int(m)
combine=[]
elements=[]
sorted_list=[]
my_dict={}
ans_list=[]
key_list=[]
set1=set()
for i in range(n):
    arr=list(map(int,input().split()))
    combine.append(arr)
#print(combine)
k=int(input())
for i in range(len(combine)):
    elements.append(combine[i][k])
    my_dict[i]=combine[i]
#print(my_dict)
#print(elements)
elements.sort()
#print(elements)
set1=set(elements)
#print(set1)
for i in set1:
    for key,v in my_dict.items():
        if i==v[k]:
            #print(v)
            #print(key)
            ans_list.append(v)
            #key_list.append(key)
#print("values are",ans_list)
#print("keys are",key_list)
for i in ans_list:
    print(*i)
