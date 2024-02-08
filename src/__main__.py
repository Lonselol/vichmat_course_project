import myLibs.helper as helper
import numpy as np
from methods import method_1, method_2, method_4

def main():
  file = open("tests.txt", "w", encoding='utf-8')
  tests = 6
  N = 4
  methods = {
  method_1.methodMonotonSweep : "Monotonic sweep",
  method_2.methodMonotonSweepModify: "Modified monotonic sweep",
  method_4.methodNotmonotonSweep: "Non-monotonic sweep"
  }
  matrixs = [np.array([[10.800, 0.0475, 0.0000, 0.0000],
                      [0.0321, 9.9000, 0.0523, 0.0000],
                      [0.0000, 0.0369, 10.000, 0.0570],
                      [0.0000, 0.0000, 0.0416, 10.100]]),]
  f = [np.array([12.143, 10.0897, 13.6744, 10.8972])]
  helper.generateMatrixs(matrixs, f, N, tests)

  for i in range(len(matrixs)):
    mat = matrixs[i]
    solution = np.linalg.solve(matrixs[i], f[i])
    helper.writeAndPrint(s=f"Matrix {i}\n", file=file)
    for j in range(len(matrixs[i])):
      helper.writeAndPrint(s=f"[", file=file)
      for x in matrixs[i][j]:
        helper.writeAndPrint(s=f"{x:.8f} ", file=file)
      helper.writeAndPrint(s=f"] {f[i][j]:.8f}\n", file=file)
    helper.writeAndPrint(s=f"condition number: {(np.linalg.norm(mat)*np.linalg.norm(np.linalg.inv(mat))):.8f}\n", file=file)
    helper.writeAndPrint(s=f"solution: ", file=file)
    for x in solution:
      helper.writeAndPrint(s=f"{x:.8f} ", file=file)
    helper.writeAndPrint(s=f"\n", file=file)
    for method, name in methods.items():
      A, B, C = helper.coefficients(mat)
      U = method(A, B, C, f[i])
      if not (isinstance(U, str)):
        helper.writeAndPrint (f"{name}\n    solution: ", file=file)
        for x in U:
          helper.writeAndPrint(s=f"{x:.8f} ", file=file)
        helper.writeAndPrint(s=f"\n", file=file)
        helper.writeAndPrint (f"    error: {(np.linalg.norm(solution - U)/np.linalg.norm(solution)*100):.8f}\n", file=file)
      else:
        helper.writeAndPrint(f"Monotonic sweep\n    {U}\n", file=file)
    helper.writeAndPrint(f"\n", file=file)
  file.close()

if __name__ == "__main__":
  main()
