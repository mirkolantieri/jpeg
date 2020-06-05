from models.dctHome import Home as h
import time
import matplotlib.pyplot as plt




#print(a)


#h.DCT2(a, N)

#\h.customDCT(a,N)


# Caso semplice


times1 = []
N = 8



for x in range(0,100,10):
    start_time = time.perf_counter()
    a = h.createMatrix(N)
    h.DCT2(a, N)
    elapsed_time = time.perf_counter() - start_time
    N = N + 2
    times1.append(elapsed_time)
    
x=[i for i in range(0,100,10)]
plt.figure()
plt.title("DCT2 FAST")
plt.xlabel("Complexity")
plt.ylabel("Time required")
plt.plot(x,times1)




times11 = []

for y in range(0,100,10):
    start_time = time.perf_counter()
    a = h.createMatrix(N)
    h.DCT2(a, N)
    elapsed_time = time.perf_counter() - start_time
    N = N + 2
    times11.append(elapsed_time)
    
y=[j for j in range(0,100,10)]
plt.figure()
plt.title("DCT2 CUSTOM")
plt.xlabel("Complexity")
plt.ylabel("Time required")
plt.plot(y,times1)

