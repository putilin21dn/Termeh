import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.animation import FuncAnimation

t, T = sp.Symbol('t'), np.linspace(1, 15, 1000)

r, phi = 1 + sp.cos(t), 1.25*t   # 20 variant
x, y = r * sp.cos(phi), r * sp.sin(phi)

Vx, Vy = sp.diff(x, t), sp.diff(y, t)  # скорость
Wx, Wy = sp.diff(Vx, t), sp.diff(Vy, t)  # ускорени

F_func = [sp.lambdify(t, i) for i in [x, y, Vx, Vy, Wx, Wy]]
[X, Y, Vx, Vy, Wx, Wy] = [func(T) for func in F_func]

fig = plt.figure()  # генерация окна

ax = fig.add_subplot(1, 1, 1)
ax.axis('equal'), ax.set_title("Модель движения точки"), ax.set_xlabel('x'), ax.set_ylabel('y'), ax.plot(X, Y), ax.set(
    xlim=[-5, 5], ylim=[-5, 5])


P = ax.plot(X[0], Y[0], marker='o')[0]
kf= 0.2

def anima(i):
    P.set_data(X[i], Y[i])
    VLine = ax.arrow(X[i], Y[i], kf * Vx[i], kf * Vy[i], width=0.02, color='red')  # Вектор скорости
    WLine = ax.arrow(X[i], Y[i], kf * Wx[i], kf * Vy[i], width=0.02, color='green')  # Вектор ускорения

    CVector = ax.arrow(X[i], Y[i], - kf * ((Vy[i] * (Vx[i] ** 2 + Vy[i] ** 2)) / (Vx[i] * Wy[i] - Wx[i] * Vy[i])),
                       kf * ((Vx[i] * (Vx[i] ** 2 + Vy[i] ** 2)) / (Vx[i] * Wy[i] - Wx[i] * Vy[i])),
                       width=0.03, color="yellow")  # Вектор кривизны

    return P, VLine, WLine, CVector

kino = FuncAnimation(fig, anima, frames=len(T), interval=5, blit=True)

plt.show()
