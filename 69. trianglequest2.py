# def myfunx(n):
#     for i in range(1,n+1):
#         print(i,end="")
#     for i in range(n-1,0,-1):
#         print(i,end="")
#     print()
# rows=int(input())
# for i in range(1,rows+1):
#     myfunx(i)

# Method 2
# for i in range(1,int(input())+1): 
#     print ((int("1"*i)*int("1"*i)))

# Method 3
# result=0
# for i in range(1,10):
#     result=result+10**i
#     print(result*result//100)

# Method 4
for i in range(1,int(input())+1): 
    print((10**i//9)**2)