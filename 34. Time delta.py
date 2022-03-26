from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))


for i in range(int(input())):
    t1=input()
    t2=input()
    delta=time_delta(t1,t2)
    print(delta)