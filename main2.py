from models.dctHome import Home as h
import time
import matplotlib.pyplot as plt


matrx = h.createMatrix(8)

"""print(matrx)


h.DCT2(matrx, 8)

h.customDCT(matrx, 8)
"""

# Caso semplice


times1 = []
N = 2

"""

for x in range(0,10,1):
    start_time = time.perf_counter()
    a = h.createMatrix(N)
    h.DCT2(a, N)
    elapsed_time = time.perf_counter() - start_time
    N = N + 5
    times1.append(elapsed_time)
    
x = [i for i in range(0,10,1)]
plt.figure()
plt.title("DCT2 FAST")
plt.xlabel("Complexity")
plt.ylabel("Time required")
plt.plot(x,times1)
plt.show()
"""


times11 = []

for y in range(0,10,1):
    start_time = time.perf_counter()
    a = h.createMatrix(N)
    h.customDCT(a, N)
    elapsed_time = time.perf_counter() - start_time
    N = N + 5
    times11.append(elapsed_time)
    
y = [j for j in range(0,10,1)]
plt.figure()
plt.title("DCT2 CUSTOM")
plt.xlabel("Complexity")
plt.ylabel("Time required")
plt.plot(y, times11)
plt.show()
