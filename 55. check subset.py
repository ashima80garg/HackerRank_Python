n=int(input())
for i in range(n):
    count=0
    m=int(input())
    setA=list(map(int,input().split()))
    n=int(input())
    setB=list(map(int,input().split()))
    for i in range (len(setA)):
        for j in range (len(setB)):
            if (setA[i]==setB[j]):  
              count+=1 
    if(count==len(setA)):
        print(True)
    else:
        print(False)