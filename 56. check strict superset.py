setA=set(map(int,(input().split())))
setA_len=len(setA)
n=int(input())
ans=[]
count=0
for i in range(n):
    set_to_test=set(map(int,input().split()))
    set_to_test_len=len(set_to_test)
    if (setA_len>set_to_test_len):
        if(set_to_test.issubset(setA)):
            count+=1
if count==n:
    print("True")
else:
    print("False")
