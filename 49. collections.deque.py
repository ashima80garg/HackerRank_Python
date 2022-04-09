from collections import deque
n=int(input())
dq=deque()
for i in range(n):
    arr=input().split()
    cmd=str(arr[0])
    if cmd=="append":
        value=int(arr[1])
        dq.append(value)
    if cmd=="appendleft":
        value=int(arr[1])
        dq.appendleft(value)
    if cmd=="pop":
        dq.pop()
    if cmd=="popleft":
        dq.popleft()
for i in dq:
        print(i,end=" ")
