cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    if n==0:
        l1=[]
        return l1
    elif n==1:
        l1=[0]
        return l1
    else:
        a=0
        b=1
        l1=[0,1]
        for i in range(n-2):
            c=a+b
            l1.append(c)
            a=b
            b=c
        return l1

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))