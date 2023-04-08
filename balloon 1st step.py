import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from math import *
def fxv(x1, x2, y, phi1, phi2):
    first = x1 + y * cos(3 * math.pi / 2 - phi1) - Ax
    second = x2 + y * cos(3 * math.pi / 2 + phi2) - Bx
    third = y + y * sin(3 * math.pi / 2 - phi1) - Ay
    fourth = (phi1 + phi2) * y + (x2 - x1) - C
    fifth = y + y * sin(3 * math.pi / 2 + phi2) - By
    X = np.array([first, second, third, fourth, fifth])
    return X
# Ax, Ay, Bx, By, C = (float(input()) for _ in range(5))

Ax = -0.353
Bx = 0.353
Ay = By = 0.3
C = 3*math.pi/8

x1 = -0.3
x2 = 0.66
y = 0.6
phi1 = 0.7
phi2 = -0.7

Xv = fxv(x1, x2, y, phi1, phi2)
Xv0 = np.array([x1, x2, y, phi1, phi2])
for i in range(100):
    Xv = fxv(x1, x2, y, phi1, phi2)
    a = (Xv - Xv0) / Xv
    if (abs(a) < 1e-10).all():
        print(Xv)
        break
    x1 = Xv0[0]
    x2 = Xv0[1]
    y = Xv0[2]
    phi1 = Xv0[3]
    phi2 = Xv0[4]
    Xv0 = Xv
x1 = Xv[0]
x2 = Xv[1]
y = y1 = y2 = Xv[2]
phi1 = Xv[3]
phi2 = Xv[4]
l = x2 - x1
alpha1 = 3*math.pi/2 - phi1
alpha2 = 3*math.pi/2
# x01 = [x1, x2]
# y01 = [y1, y2]

fig, ax = plt.subplots()
arc_x = x2
arc_y = y2+0.01
arc_width = 0.02
arc_height = 0.02
arc_theta1 = 270
arc_theta2 = math.degrees(abs(phi2))+180
arc = patches.Arc((arc_x, arc_y),
                                 arc_width,
                                 arc_height,
                                 theta1=arc_theta1,
                                 theta2=arc_theta2)
ax.add_patch(arc)
arc_x = x1
arc_y = y1+0.01
arc_theta1 = -math.degrees(abs(phi1))
arc_theta2 = 270
arc = patches.Arc((arc_x, arc_y),
                                 arc_width,
                                 arc_height,
                                 theta1=arc_theta1,
                                 theta2=arc_theta2)
ax.add_patch(arc)
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

x01 = [x1, x2]
y01 = [y1, y2]
x02 = [x1+arc_height/2, x2-arc_height/2]
# print(arc_radius)
y02 = [y1 + 0.01 - 0.5 * arc_height * sin(phi1), y2 + 0.01 - 0.5 * arc_height * sin(phi2)]
ax.plot(x01, y01)
ax.plot(x02, y02)

plt.axis('equal')
plt.show()
