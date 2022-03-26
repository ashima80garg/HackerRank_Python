import math

AB = int(input())
BC = int(input())
theta=math.atan(AB/BC)
theta=round(math.degrees(theta))
print(theta,chr(176),sep='')