import numpy as np

def methodMonotonSweepModify(A, B, C, F):
  N = len(A)
  U = np.zeros(N)
  #Initial values
  lambda_max = max(F[0], B[0], C[0])
  alpha = np.zeros(N)
  beta = np.zeros(N)
  gamma = np.zeros(N)
  alpha[0] = B[0] / lambda_max
  beta[0] = C[0] / lambda_max
  gamma[0] = F[0] / lambda_max

  #Forward
  for k in range(1, N):
    alpha_k = alpha[k - 1] * B[k] - beta[k - 1] * A[k]
    beta_k = alpha[k-1] * C[k]
    gamma_k = alpha[k-1] * F[k] - gamma[k - 1] * A[k]
    max_k = max(alpha_k, beta_k, gamma_k)
    alpha[k] = alpha_k / max_k
    beta[k] = beta_k / max_k
    gamma[k] = gamma_k / max_k

  #Backward
  N = N - 1
  U[N] = (A[N]*gamma[N-1]-alpha[N-1]*F[N])/(A[N]*beta[N-1]-alpha[N-1]*B[N])
  U[N-1] = (F[N] * beta[N-1] - gamma[N-1] * B[N]) / (A[N] * beta[N-1] - alpha[N-1] * B[N])
  N += 1
  for i in range(N-3, -1, -1):
    if alpha[i] == 0:
      U[i] = (F[i+1]-B[i+1]*U[i+1]-C[i+1]*U[i+2])/A[i+1]
      print(U[i])
    else:
      U[i] = (gamma[i]-beta[i]*U[i+1])/alpha[i]
  return U
