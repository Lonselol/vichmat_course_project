import numpy as np

def methodMonotonSweep(A, B, C, F):
  N = len(A)
  for i in range (1, N - 1):
    if np.abs(B[i]) < (np.abs(C[i]) + np.abs(A[i])):
      return "does not meet the condition"
  for i in range(N):
    if B[i] == 0:
      return "zeroes on the main diagonal"
  U = np.zeros(N)

  #Forward
  alpha = np.zeros(N)
  beta = np.zeros(N)
  alpha[0] = -C[0] / B[0]
  beta[0] = F[0] / B[0]
  for k in range(0, N-1):
    alpha[k+1] = -C[k] / (B[k] + A[k] * alpha[k])
    beta[k+1] = (F[k] - A[k] * beta[k]) / (B[k] + A[k] * alpha[k])
    
  #Backward
  U[N-1] = (F[N-1] - A[N-1] * beta[N-1]) / (A[N-1] * alpha[N-1] + B[N-1])
  for i in range(N - 2, -1, -1):
    U[i] = alpha[i + 1] * U[i + 1] + beta[i + 1]
  return U
