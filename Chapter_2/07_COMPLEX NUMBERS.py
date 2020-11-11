from math import sqrt

def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)


def cMult(u,v):
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]


def mandelbrot(z,num):
    count=0
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    return num

