# Variant 29
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
import math



def Circle2(X, Y, radius):
    CX = [X + radius * math.cos(i/100) for i in range(0, 628)]
    CY = [Y + radius * math.sin(i/100) for i in range(0, 628)]
    return CX, CY


def Circle3(X, Y):
    CX = [X + 0.75 * 0.5 * math.cos(i/100) for i in range(0, 628)]
    CY = [Y + 0.75 * 0.5 * math.sin(i/100) for i in range(0, 628)]
    return CX, CY


Frames = 100
Interval_Frame = 0
Repeat_Delay_Anim = 0

# radius = math.pi/4 * 5
radius = 3
beam_length = 1

t = sp.Symbol('t')

phi = math.pi / 4 * t
psi = math.pi / 4 * 5 * t

# speed and acceleration of point A
xa = sp.sin(phi) * radius
ya = sp.cos(phi) * radius
vxa = sp.diff(xa, t)
vya = sp.diff(ya, t)
wxa = sp.diff(vxa, t)
wya = sp.diff(vya, t)
va = (vxa**2 + vya**2)**0.5
wa = (wxa**2 + wya**2)**0.5

# speed and acceleration of point B (without A)
xb = sp.sin(psi) * beam_length
yb = sp.cos(psi) * beam_length
vxb = sp.diff(xb, t)
vyb = sp.diff(yb, t)
wxb = sp.diff(vxb, t)
wyb = sp.diff(vyb, t)
vb = (vxb**2 + vyb**2)**0.5
wb = (wxb**2 + wyb**2)**0.5

T = np.linspace(0, Frames, 1000)
XA = np.zeros_like(T)
YA = np.zeros_like(T)
XB = np.zeros_like(T)
YB = np.zeros_like(T)

for i in np.arange(len(T)):
    XA[i] = sp.Subs(xa, t, T[i])
    YA[i] = sp.Subs(ya, t, T[i])
    XB[i] = sp.Subs(xb, t, T[i])
    YB[i] = sp.Subs(yb, t, T[i])


fig = plt.figure(figsize=(17, 8))

ax = fig.add_subplot(1, 2, 1)
ax.axis('equal')
ax.set(xlim=[-10, 10], ylim=[-10, 10])

Beam = ax.plot([XA[0], XA[0] + XB[0]], [YA[0], YA[0] + YB[0]], 'green')[0]
circle2 = ax.plot(*Circle2(0, 0, radius), 'red')[0]  # main circle
circle3 = ax.plot(*Circle3(XA[0] + XB[0], YA[0] + YB[0]), 'green')[0]  # point B


def anima(i):
    Beam.set_data([XA[i], XA[i] + XB[i]], [YA[i], YA[i] + YB[i]])
    circle2.set_data(*Circle2(0, 0, radius))  # main circle
    circle3.set_data(*Circle3(XA[i] + XB[i], YA[i] + YB[i]))  # small circle
    return Beam, circle2, circle3


kino = FuncAnimation(fig, anima, frames=Frames, interval=Interval_Frame,
                     blit=False, repeat=True, repeat_delay=Repeat_Delay_Anim)

plt.show()
