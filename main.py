import math, random
from matplotlib import pyplot as plt

n = 14
N = 256
w = 1800
values = [[0 for _ in range(N)] for _ in range(N)]
F = [0 for _ in range(N)]
Fih = [0 for _ in range(N)]

def get_signal(w, n, xmin=0, xmax=1):
    A = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    fi = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    def f(t):
        x = 0
        for i in range(n):
            x += A[i] * math.sin(w/n*t*i + fi[i])
        return x
    return f

def calcFi(Fih):
    for i in range(0,N):
        Fih[i] = -(2*math.pi)*(i/10.0)
    return Fih

def get_table(values,Fih):
    for i in range(0,N):
        for j in range(0,N):
            temp = i*j
            if temp < N:
                values[i][j] = math.cos(Fih[temp]) + math.sin(Fih[temp])
            else:
                temp %= N
                values[i][j] = math.cos(Fih[temp]) + math.sin(Fih[temp])
    return values

def calcFp(F, signal, values):
    for i in range(0,N):
        for j in range(0, N):
            F[i] += signal[j]*values[i][j]
    return F

gen = get_signal(w, n)
S = [gen(i) for i in range(0,N)]
Fih = calcFi(Fih)
values = get_table(values,Fih)
F = calcFp(F, S, values)

fig = plt.figure()
ax_1 = fig.add_subplot(2, 1, 1)
ax_2 = fig.add_subplot(2, 1, 2)
ax_1.plot(range(0,N), S)
ax_2.plot(range(0, N), F)
plt.show()