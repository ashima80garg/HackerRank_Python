n=int(input())
l=list(map(int,input().split()))
#l=[12,3,4,-5]
l1=[]
x=0
y=0
for i in range(len(l)):
    if l[i]>0:
        l1.append(l[i])   
if (len(l)==len(l1)):
        #print("all positive")
        x=1
#else:
       # print("no")
l=list(map(str,l))
for ele in l:
        no=ele
        ans=[]
        reverse=[]
        l=len(no)
        for i in no:
                #print(i)
                ans.append(i)
        #print(''.join(ans))
        end=l-1
        #print("end is",end)
        while(end>=0):
                reverse.append(ans[end])
                end-=1
        #print(''.join(reverse))
        if ans==reverse:
                #print("yes")
                y=1
        #else:
                #print("no")
if x==1 and y==1:
        print("True")
else:
        print("False")
