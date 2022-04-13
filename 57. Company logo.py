import collections
str=list(input())
count=0
freq=[]
ans_l=[]
l1=[]
l2=[]
sorted_ans=[]
s1={}
#print(str)
d=dict(collections.Counter(str))
#print(d)
for k,v in d.items():
    freq.append(v)
freq.sort(reverse=True)
#print(freq)
f1=freq[0]
f2=freq[1]
f3=freq[2]
#print(f1)
#print(f2)
#print(f3)
if(f1==f2==f3):
    #print("case1")
    for key,val in d.items():
        #print("key is",key)
        ans_l.append(key)
        sorted_ans=sorted(ans_l)
        #print(sorted_ans)
    print(sorted_ans[0],f1)    
    print(sorted_ans[1],f1) 
    print(sorted_ans[2],f1) 
elif (f1!=f2!=f3):
    #print("case2")
    for key,val in d.items():
        if val==f1:
            print(key,f1)
    for key,val in d.items():
        if val==f2:
            print(key,f2)
    for key,val in d.items():
        if val==f3:
            print(key,f3)
else:
    #print("case3")
    if(f1==f2):
        for key,val in d.items():
            if val==f1:
                #print("most occuring is {} with f {}".format(key,f1))
                l1.append(key)
                #print("list is",l1)
        ans_l=sorted(l1)
        #print("sorted list is",ans_l)
        print(ans_l[0],d.get(ans_l[0]))
        print(ans_l[1],d.get(ans_l[1]))
        for key,val in d.items():
            if val==f3:
                print(key,f3)
    if(f2==f3):
        for key,val in d.items():
            if val==f2:
                #print("most occuring is {} with f {}".format(key,f1))
                l1.append(key)
                #print("list is",l1)
        ans_l=sorted(l1)
        #print("sorted list is",ans_l)
        for key,val in d.items():
            if val==f1:
                print(key,f1)
        print(ans_l[0],d.get(ans_l[0]))
        print(ans_l[1],d.get(ans_l[1]))
        