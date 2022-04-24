s=input()
lower=[]
upper=[]
odd=[]
even=[]
ans_list=[]
for i in s:
    if i.islower():
        lower.append(i)
        lower.sort()
#print(lower)
for i in s:
    if i.isupper():
        upper.append(i)
        upper.sort()
#print(upper)
for i in s:
    if i.isdigit():
        i=int(i)
        val=i%2
        if (val==0):
            even.append(i)
            even.sort()
        else:
            odd.append(i)
            odd.sort()
#print(even)
#print(odd)
ans_list.append(lower)
ans_list.append(upper)
ans_list.append(odd)
ans_list.append(even)
#print(ans_list)
for i in ans_list:
    for j in i:
        print(j,end='')