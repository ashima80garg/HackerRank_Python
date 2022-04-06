n=int(input())
country=[]
result=[]
for i in range(n):
    arr=input()
    country.append(arr)
count=0
for i in country:
    if i not in result:
        result.append(i)
        count+=1    
print(count)