import numpy as np

n = 3
A = np.random.rand(n, n)

spectral_norm = np.linalg.norm(A, 2)
M_A = n * np.max(np.abs(A))

if (1/n) * M_A <= spectral_norm <= M_A:
    print("True")
else:
    print("False")
