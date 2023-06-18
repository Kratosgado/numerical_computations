import numpy as np

# function to display 3x1 matrix
def displayValues(arr):
    var = ['x', 'y', 'z']
    for i in range(3):
        print(f"{var[i]} = {arr[i]}")

# The matrix
A = np.array([
    [28,21,5],
    [7,17,3],
    [12,11,24]
])

b = np.array([
    [1000],
    [500],
    [750]
])
tolerance = 0.01
w = 0.7

# initial solution
x0 = np.array([
    [26],
    [26],
    [26]
])

# lower triangular matrix from A
L = np.array([
    [0,0,0],
    [7,0,0],
    [12,11,0]
])
# Diagonal matrix from A
D = np.array([
    [28,0,0],
    [0,17,0],
    [0,0,24]
])
# Upper triangular matrix from A
U = np.array([
    [0,21,5],
    [0,0,3],
    [0,0,0]
])


wLD_inverse = np.linalg.inv(w * L + D) # calculates (wL + D) inverse
wLD_inverse = np.round(wLD_inverse,4) # rounds it to 4dp

print(f"(wL + D)inverse =  \n {wLD_inverse}")

# calculates wU
# calculated separately because It's constant in the equation
wU = w * U
print(f"wU = \n {wU}")

wLD_inverse_b = np.dot((w * wLD_inverse), b) # calculates w(wL + D) inverse * b
wLD_inverse_b = np.round(wLD_inverse_b, 4) # rounds it to 4dp
print(f"w(wL + D)inverse x b = \n {wLD_inverse_b}")

wD1 = (1 - w) * D # calculates (1 - w)D, It's also a constant
print(f"(1-w)D = \n {wD1}")

# This function calculates for the next guess
def findNext(sol):
    print(f"current values")
    displayValues(sol)                      # display the current guess values
    wD1x = np.round(np.dot(wD1, sol), 4)    # calculates (1-w)Dx in 4dp
    wUx = np.round(np.dot(wU, sol), 4)      # calculates wUx in 4dp
    wD1x_sub_wUx = np.subtract(wD1x, wUx)   # calculates (1-w)Dx - wUx
    wLD_inverse_x_wD1x_sub_wUx = np.round(np.dot(wLD_inverse, wD1x_sub_wUx), 4) # calculates [(wL+D)inverse][(1-w)Dx - wUx]
    new_sol = np.add(wLD_inverse_x_wD1x_sub_wUx, wLD_inverse_b) # calculates [(wL+D)inverse][(1-w)Dx - wUx] + [w(wL+D)inverse]b

    print(f"(1-w)Dx - uUx =")
    displayValues(wD1x_sub_wUx) 
    print(f"")

    return new_sol # return the new calculated value

x1 = findNext(x0)
iteration = 1
while (abs(x1[0] - x0[0]) > tolerance and iteration < 9):
    print(f"\n \t\t ITERATION: {iteration}")
    print(f"Absolute difference= {abs(x1[0] - x0[0])}", end="\n")
    x0 = x1
    x1 = findNext(x1)
    iteration += 1

print(f"Iteration 8 ")
print(f"Absolute difference= {abs(x1[0] - x0[0])}", end="\n")
displayValues(x1)


# print(wLD_inverse_b)
