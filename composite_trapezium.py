import numpy as np

# define the function in this function
def f(x):
    return 2 * x**2

def find_composite_trapezium(upper_limit, lower_limit, N):
    h = (upper_limit - lower_limit) / float(N)
    """
    Calculates the definite integral of a function using composite trapezium rule.

    :param upper_limit: float, the upper limit of the integral
    :param lower_limit: float, the lower limit of the integral
    : parameter N : the number of subdivisions
    :param h: float, the interval width
    :return: float, the approximate value of the integral
    """
    I_x = 0
    for x in np.arange(lower_limit, upper_limit+h, h):
        print(x)
        if (x == lower_limit or x == upper_limit):
            I_x += f(x)
        else:
            I_x += 2 * f(x)
    return h * 0.5 * I_x
    