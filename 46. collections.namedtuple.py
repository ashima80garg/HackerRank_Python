from collections import namedtuple
n=int(input())
sum=0
x,y,z,w=input().split()
if x=="MARKS":
    desired_col=0
elif y=="MARKS":
    desired_col=1
elif z=='MARKS':
    desired_col=2
else:
    desired_col=3
student=namedtuple('student',[x,y,z,w])
for i in range(n):
    a,b,c,d=input().split()
    s1=student(a,b,c,d)
    #print(s1._fields)
    #print(s1[1])
    sum+=int(s1[desired_col])
print(sum/n)
