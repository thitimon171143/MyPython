import math
a = float(input('ความยาวด้าน a : '))
b = float(input('ความยาวด้าน b : '))
D = float(input('มุม C : '))
C = D*math.pi/180
c = math.sqrt(a**2+b**2-2*a*b*math.cos(C))
print('ความยาวด้าน c : ',c)