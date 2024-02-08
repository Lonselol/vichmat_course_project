import numpy as np

#Iint
n = 3
A = np.random.rand(n, n)
f = np.random.rand(n)

sigma = np.random.rand()
x = np.random.rand(n)

#condNumber
cond_A = np.linalg.cond(A)
cond_A_sigma = np.linalg.cond(A + sigma * A)

#Check
left_side = sigma * x / (x + sigma * x)
right_side = cond_A * sigma * A / A
if np.all(left_side <= right_side):
    print("True")
else:
    print("False")
