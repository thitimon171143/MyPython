import math
a = float(input())
b = float(input())
C = float(input())
CR = C*math.pi/180
area = 1/2*a*b*math.sin(CR)
print("area =",area,"(sq cm)")