import numpy as np
import math
from matplotlib import pyplot as pp

def f(x):
    return np.sin(x)
def deriv(x):
    return np.cos(x)

a=0
def taylor(x,terms):
    value=0
    for i in range(terms+1):
        if (i % 4 == 0):
            value += ((f(a)/math.factorial(i))*(x-a)**i)
        elif (i % 4 == 1):
            value += ((deriv(a)/math.factorial(i))*(x-a)**i)
        elif (i % 4 == 2):
            value += ((-f(a)/math.factorial(i))*(x-a)**i)
        else:
            value += ((-deriv(a)/math.factorial(i))*(x-a)**i)
    return value

estimate = taylor(2,15)
print(estimate)

values=[-10]
temp=-9.9
while (values[-1] < 10):
    values.append(temp)
    temp+=0.1

result=[]
for i in range(199):
    result.append(taylor(values[i],15))

pp.plot(result,values)
pp.savefig('taylor.png')