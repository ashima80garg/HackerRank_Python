m = int(input())
s = set(map(int, input().split()))
n=int(input())
for i in range(n):
    arr=input().split()
    cmd=str(arr[0])
    if cmd=="pop":
        s.pop()
    if cmd=="remove":
        value=int(arr[1])
        s.remove(value)
    if cmd=="discard":
        value=int(arr[1])
        s.discard(value)
    
print(sum(s))
