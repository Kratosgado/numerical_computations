import numpy as np

def f(x):
    return 2 * x**2

def find_composite_trapezium(upper_limit, lower_limit, h):
    I_x = 0
    for x in np.arange(lower_limit, upper_limit+h, h):
        print(x)
        if (x == lower_limit or x == upper_limit):
            I_x += f(x)
        else:
            I_x += 2 * f(x)
    return h * 0.5 * I_x
    
def find_composite_simpson():
    pass

def romberg_method():
    pass

print(find_composite_trapezium(5,3,0.5))

