def f(x):
    return (x**2) + 2*x - 3


def findRoot(a, b):
    if ((f(a) * f(b)) >= 0):
        return f"range [{a},{b}] will not converge"
    
    counter = 0
    c = (a+b)/2.0
    while (b - c > 0.05):
        counter += 1
        print(f"Iteration {counter}\n")
        print(f"a = {a} \t b = {b} \t c = {c} \nb - c = {b - c} \t f(a) * f(c) = {f(a) * f(c)}\n")
        if(f(a) * f(c) <= 0):
            b = c
        else:
            a = c
        c = (a+b)/2.0
    print("Root = " , c)
    return c

print(findRoot(0,2))
# print(f(0) * f(2))