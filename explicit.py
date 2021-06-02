import numpy as np
import math
import matplotlib.pyplot as plt

pi = math.pi
a = 2/pi**2
l = 6
m = 100
n = 10
T = 5
h = l/n
tau = T/m
x = np.zeros(n+1)
t = np.zeros(m+1)
for i in range(n+1):
    x[i] = i*h
for k in range(m+1):
    t[k] = k*tau
gamma = ((a**2)*tau)/(h**2)
U = np.zeros((m+1, n+1))


def initialCondition(x):
    return math.sin(pi*x/2)


for k in range(m+1):
    for i in range(n+1):
        U[0, i] = initialCondition(x[i])
        U[k, n] = t[k]

for k in range(0, m):
    U[k, 0] = U[k, 1]
    for i in range(1, n):
        U[k+1, i] = (((a**2)*((U[k, i-1]-2*U[k, i]+U[k, i+1])/(h**2)))+1)*tau+U[k, i]

y0 = []
for k in range(0, m+1):
    y0 = []
    for i in range(0, n+1):
        y0.append(U[k, i])
    if ((t[k] == 0) or (t[k] == 0.2) or (t[k] == 0.4) or (t[k] == 0.6) or (t[k] == 0.8) or (t[k] == 1)):
        plt.plot(x, y0, label="t = %.1f" %t[k])

plt.title("Явная схема")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc=0)
plt.show()
