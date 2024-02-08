import numpy as np

def coefficients(A_matrix):
  N = A_matrix.shape[0]
  A = np.zeros(N)
  B = np.zeros(N)
  C = np.zeros(N)
  B = A_matrix.diagonal()
  for i in range(1, N):
    C[i] = np.copy(A_matrix[i-1][i])
  for i in range(0, N-1):
    A[i] = np.copy(A_matrix[i+1][i])
  return A, B, C

def writeAndPrint(s, file):
  print(s)
  file.write(s)
  return

def generateMatrixs(matrixs, f, N, tests):
  for i in range(tests):
    newM = np.random.uniform(low=-9, high=9, size=(N, N))
    newF = np.random.uniform(low=0, high=9, size = N)
    matrixs.append(newM)
    f.append(newF)
