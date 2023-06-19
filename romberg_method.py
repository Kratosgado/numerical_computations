import numpy as np
from IPython.display import display, Math
import math

# 26 * x * (math.exp(x))
def f(x):
    return 1/(1+x)

def find_composite_trapezium(upper_limit, lower_limit, h):
    I_x = 0
    for x in np.arange(lower_limit, upper_limit+h, h):
        if (x == lower_limit or x == upper_limit):
            I_x += f(x)
        else:
            I_x += 2 * f(x)
    return h * 0.5 * I_x
    
def find_composite_simpson(upper_limit, lower_limit, h):
    I_x = 0
    counter = 0
    n = (upper_limit - lower_limit)/h
    print(n)
    for x in np.arange(lower_limit, upper_limit+h, h):
        if (counter == 0 or counter == n):
            I_x += f(x)
        elif(counter%2==1):
            I_x += 4 * f(x)
        else:
            I_x += 2 * f(x)
        counter += 1
    return h * (1/3.0) * I_x

def romberg_trapezium_method(upper_limit, lower_limit, N):
    h = (upper_limit - lower_limit) / float(N)
    
    I_x = []
    for m in range(1, 4):
        print(m)
        I0_h = find_composite_trapezium(upper_limit, lower_limit, h/float(m))
        print(I0_h)
        I0_h_2 = find_composite_trapezium(upper_limit, lower_limit, (h/2)/float(m))
        print(I0_h_2)
        Im_h = ((4**m) * I0_h_2 - I0_h)/ (4**m - 1)

        I_x.append(Im_h)
    return I_x

def romberg_simpson_method(upper_limit, lower_limit, N):
    h = (upper_limit - lower_limit) / float(N)
    
    I_x = []
    for m in range(1, 4):
        print(m)
        I0_h = find_composite_trapezium(upper_limit, lower_limit, h/float(m))
        print(I0_h)
        I0_h_2 = find_composite_trapezium(upper_limit, lower_limit, (h/2)/float(m))
        print(I0_h_2)
        Im_h = ((4**(m+1)) * I0_h_2 - I0_h)/ (4**(m+1) - 1)

        I_x.append(Im_h)
    return I_x


print(romberg_simpson_method(1, 0,2))

# print(romberg_trapezium_method(1, 0,2))

