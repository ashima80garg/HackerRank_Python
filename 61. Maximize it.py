from itertools import product
n,m=input().split()
n=int(n)
m=int(m)
ans=0
max_list = []
all_list = []
for i in range(n):
    arr = list(map(int,input().split()))
    arr_ = [i*i for i in arr[1:]]
    all_list.append(arr_)
permuted_lists = list(product(*all_list))
#print(permuted_lists)
ans=[]
for i in permuted_lists:
    sum_arr=0
    for j in i:
        sum_arr=sum_arr+j
        #print(sum_arr)
        a=sum_arr%m
        ans.append(a)
print(max(ans))