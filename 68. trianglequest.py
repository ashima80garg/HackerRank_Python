# rows=int(input())
# x=1
# for i in range(1,rows):
#     for j in range(x):
#         print(i,end="")
#     print()
#     x+=1

# Method 2
# for i in range(1,int(input())): 
#     print(int("1"*i)*i)

# Method 3
# result=0
# for i in range(1,10):
#     result=result+10**i
#     print(result*i//10)

# Method 4
for i in range(1,int(input())):
    print((10**i//9)*i)