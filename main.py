import math, random
from matplotlib import pyplot as plt

n = 14
N = 256
w = 1800

def get_signal(w, n, xmin=0, xmax=1):
    A = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    fi = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    def f(t):
        x = 0
        for i in range(n):
            x += A[i] * math.sin(w/n*t*i + fi[i])
        return x
    return f

def get_F(x):
    N = len(x)
    FR = []
    Fi = []
    for p in range(N):
        FR.append(0)
        Fi.append(0)
        for k in range(N):
            FR[p] += x[k]*math.cos(-2*math.pi*p*k/N)
            Fi[p] += x[k]*math.sin(-2*math.pi*p*k/N)
    return FR, Fi

def get_Fopt(x):
    N = len(x)
    w = []
    for i in range(N):
        if i < N//4:
            w.append((math.cos(-2*math.pi*i/N),
                      math.sin(-2*math.pi*i/N)))
        elif i < N//2:
            w.append((w[i-N//4][1],
                      -w[i-N//4][0]))
        else:
            w.append((-w[i-N//2][0], -w[i-N//2][1]))
    FR = []
    Fi = []
    for i in range(N):
        FR.append(sum([w[(i*j)%N][0]*x[j] for j in range(N)]))
        Fi.append(sum([w[(i*j)%N][1]*x[j] for j in range(N)]))
    return FR, Fi

gen = get_signal(w, n)
S = [gen(i) for i in range(0,N)]
(Fr, Fi) = get_F(S)
(Fr_1, Fi_1) = get_Fopt(S)
F = [Fr[i] + Fi[i] for i in range(N)]

fig = plt.figure()
ax_1 = fig.add_subplot(3, 2, 1)
ax_2 = fig.add_subplot(3, 2, 2)
ax_3 = fig.add_subplot(3, 2, 3)
ax_4 = fig.add_subplot(3, 2, 4)
ax_5 = fig.add_subplot(3, 2, 5)
ax_6 = fig.add_subplot(3, 2, 6)

ax_1.plot(range(N), Fr)
ax_2.plot(range(N), Fi)
ax_3.plot(range(N), Fr_1)
ax_4.plot(range(N), Fi_1)
ax_5.plot(range(N), S)
ax_6.plot(range(N), F)

ax_1.set(title='Fr')
ax_2.set(title='Fi')
ax_3.set(title='Fr_opt')
ax_4.set(title='Fi_opt')
ax_5.set(title='S')
ax_6.set(title='F')

plt.show()