import numpy as np

def f(x):
    return np.tanh(x)-0.5*x

def deriv(x):
    return (1/np.cosh(x))**2-0.5

def bisect(a,b,midpoint,tol):
    count=0
    while(np.abs(f(midpoint)) > tol):
        if((f(midpoint)*f(a))>0):
            a=midpoint
        else:
            b=midpoint
        midpoint=((a+b)/2)
        count +=1
    return midpoint, count

def Newton(p,tol,deltap):
    count=0
    while(np.abs(f(p)) > tol and np.abs(deltap) > tol):
        newp=p-(f(p)/deriv(p))
        deltap=p-newp
        p=newp
        count+=1
    return p, count

a=1
b=4
midpoint=2.5
p=2.5
deltap=5
tol = 1e-5

ans=bisect(a,b,midpoint,tol)
print("The bisection method returned a zero of",ans[0],"after",ans[1],"iterations")
ans2=Newton(p,tol,deltap)
print("The Newton-Raphson method returned a zero of",ans2[0],"after",ans2[1],"iterations")