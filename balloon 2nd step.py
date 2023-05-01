from math import cos, sin
from math import pi as pi
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np

Ax = 0.
Ay = 0.95 * 2
Bx = 0.3 * 2
By = 0.65 * 2
xTop = 0.
yTop = 0.65 * 2
xBot = 0.
yBot = 0.22 * 2
rt = 0.3 * 2
rb = 0.19 * 2
pt0 = 12000 * 2
pb0 = 4000 * 2
phi1_nd = 2.753364902
phi2_nd = 1.182568575
phi3_nd = 0.7764555030
phi4_nd_plus_phi5_nd = 5.001905970
alpha5 = (3 * pi) / 2
x5 = x4 = 0
pt = pb = p = 0.
# alpha4 = (3 * math.pi) / 2 - phi4


def F(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, r1, r2, r3, r4, r5, phi1, phi2, phi3, phi4, phi5, alpha1, alpha2, alpha3,
      alpha4, alpha5):
    f = [0] * 25
    f[0] = r1 * phi1 - rt * phi1_nd
    f[1] = r2 * phi2 - rt * phi2_nd
    f[2] = r3 * phi3 - rt * phi3_nd
    f[3] = r4 * phi4 + r5 * phi5 - rb * phi4_nd_plus_phi5_nd

    f[4] = r1 * cos(alpha1) + x1 - Ax
    f[5] = r1 * sin(alpha1) + y1 - Ay

    f[6] = r2 * cos(phi2 + alpha2) + x2 - Bx
    f[7] = r2 * sin(phi2 + alpha2) + y2 - By

    f[8] = r3 * cos(alpha3 + phi3) + x3 - r2 * cos(alpha2) - x2
    f[9] = r3 * sin(alpha3 + phi3) + y3 - r2 * sin(alpha2) - y2
    f[10] = r3 * cos(alpha3 + phi3) + x3 - r5 * cos(alpha5 + phi5) - x5
    f[11] = r3 * sin(alpha3 + phi3) + y3 - r5 * sin(alpha5 + phi5) - y5

    f[12] = r1 * cos(alpha1 + phi1) + x1 - r3 * cos(alpha3) - x3
    f[13] = r1 * sin(alpha1 + phi1) + y1 - r3 * sin(alpha3) - y3
    f[14] = r1 * cos(alpha1 + phi1) + x1 - r4 * cos(alpha4) - x4
    f[15] = r1 * sin(alpha1 + phi1) + y1 - r4 * sin(alpha4) - y4

    f[16] = x4 - x5
    f[17] = -r4 + y4 + r5 - y5

    f[18] = pt * r1 * sin(alpha1 + phi1) - (pt - pb) * r3 * sin(alpha3) - pb * r4 * sin(alpha4)
    f[19] = -pt * r1 * cos(alpha1 + phi1) + (pt - pb) * r3 * cos(alpha3) + pb * r4 * cos(alpha4)

    f[20] = -(pt - p) * r2 * sin(alpha2) + (pt - pb) * r3 * sin(alpha3 + phi3) + (pb - p) * r5 * sin(alpha5 + phi5)
    f[21] = (pt - p) * r2 * cos(alpha2) - (pt - pb) * r3 * cos(phi3 + alpha3) - (pb - p) * r5 * cos(alpha5 + phi5)

    f[22] = pb * r4 - (pb - p) * r5
    f[23] = alpha4 - 3 * pi / 2 + phi4
    f[24] = alpha5 - 3 * pi / 2
    return f

# objection!!!!!
def objective(x):

    f = F(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14],
          x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24])

    return sum([val ** 2 for val in f])


# gradient in question
def gradient(x):
    eps = 1e-5
    grad = []
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += eps
        x_minus = x.copy()
        x_minus[i] -= eps
        grad.append((objective(x_plus) - objective(x_minus)) / (2 * eps))
    return np.array(grad)

# descent (to hell i suppose)
def gradient_descent(initial_x, learning_rate=0.01, max_iter=10000, tolerance=1e-8):
    x = initial_x
    for i in range(max_iter):
        grad = gradient(x)
        if np.linalg.norm(grad) < tolerance:
            break
        x -= learning_rate * grad
    return x

x = [1.0]*25

result = gradient_descent(x)
print(result)
