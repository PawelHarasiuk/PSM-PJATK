import math
from matplotlib import pyplot as plt

G = 6.6743e-11
Ms = 1.989e30
Mz = 5.972e24
Mk = 7.347e22
RZS = 1.5e8 * 1000
RZK = 384400 * 1000
t_end = 366 * 24 * 60 * 60
dt = 3600


def Ziemia_Ksiezyc():
    list_x = []
    list_y = []
    t_start = 0
    sx = 0
    sy = RZK
    vx = math.sqrt(G * Mz / RZK)
    vy = 0

    while t_start < t_end:
        wx = -sx
        wy = -sy
        w_len = math.sqrt(wx ** 2 + wy ** 2)
        ux = wx / w_len
        uy = wy / w_len
        a = G * Mz / w_len ** 2
        ax = ux * a
        ay = uy * a

        vx_2 = vx + ax * dt / 2
        vy_2 = vy + ay * dt / 2
        dsx = vx_2 * dt
        dsy = vy_2 * dt

        sx_2 = sx + vx_2 * dt / 2
        sy_2 = sy + vy_2 * dt / 2

        list_x.append(sx_2)
        list_y.append(sy_2)

        wx_2 = -sx_2
        wy_2 = -sy_2
        w_len_2 = math.sqrt(wx_2 ** 2 + wy_2 ** 2)
        ux_2 = wx_2 / w_len_2
        uy_2 = wy_2 / w_len_2
        a_2 = G * Mz / w_len_2 ** 2
        ax_2 = ux_2 * a_2
        ay_2 = uy_2 * a_2
        dvx = ax_2 * dt
        dvy = ay_2 * dt

        sx += dsx
        sy += dsy
        vx += dvx
        vy += dvy
        t_start += dt

    return list_x, list_y


def Slonce_Ziemia():
    list_x = []
    list_y = []
    t_start = 0
    sx = 0
    sy = RZS
    vx = math.sqrt(G * Ms / RZS)
    vy = 0

    while t_start < t_end:
        wx = -sx
        wy = -sy
        w_len = math.sqrt(wx ** 2 + wy ** 2)
        ux = wx / w_len
        uy = wy / w_len
        a = G * Ms / w_len ** 2
        ax = ux * a
        ay = uy * a

        vx_2 = vx + ax * dt / 2
        vy_2 = vy + ay * dt / 2
        dsx = vx_2 * dt
        dsy = vy_2 * dt

        sx_2 = sx + vx_2 * dt / 2
        sy_2 = sy + vy_2 * dt / 2

        list_x.append(sx_2 / 10)
        list_y.append(sy_2 / 10)

        wx_2 = -sx_2
        wy_2 = -sy_2
        w_len_2 = math.sqrt(wx_2 ** 2 + wy_2 ** 2)
        ux_2 = wx_2 / w_len_2
        uy_2 = wy_2 / w_len_2
        a_2 = G * Ms / w_len_2 ** 2
        ax_2 = ux_2 * a_2
        ay_2 = uy_2 * a_2
        dvx = ax_2 * dt
        dvy = ay_2 * dt

        sx += dsx
        sy += dsy
        vx += dvx
        vy += dvy
        t_start += dt

    return list_x, list_y


def polozenie(x_k, y_k, x_s, y_s):
    fig, ax = plt.subplots()
    ax.plot(x_k, y_k, label='ksiezyc')
    ax.plot(x_s, y_s, label='ziemia')

    ax.legend()

    plt.grid(True)
    plt.show()


def Slonce_Ksiezyc():
    x = []
    y = []

    x1, y1 = Slonce_Ziemia()
    x2, y2 = Ziemia_Ksiezyc()

    for i in range(len(x1)):
        x.append(x1[i] + x2[i])
        y.append(y1[i] + y2[i])
    return x, y


x, y = Slonce_Ksiezyc()
x1, y1 = Slonce_Ziemia()
polozenie(x, y, x1, y1)
