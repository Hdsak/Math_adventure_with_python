import math


def harmonograph(t):
    a1=a2=a3=a4 = 100
    f1,f2,f3,f4 = 2.01,3,3,2
    p1,p2,p3,p4 = -math.pi / 2, 0, -math.pi /16,0
    d1,d2,d3,d4 = 0.00085,0.0065,0,0
    x = a1*math.cos(f1*t + p1)*math.exp(d1*t) + a3*math.cos(f3*t + p3)*math.exp(d3*t)
    y = a2*math.sin(f2*t + p2)*math.exp(d2*t) + a4*math.sin(f4*t + p4)*math.exp(d4*t)
    return [x,y]