import math

from matplotlib import pyplot as plt

dt = 0.05
r = 2
h = 20
m = 1
g = 9.81
Ik = 2 / 5 * m * r ** 2
alfa = math.radians(45)
d90 = math.radians(90)
acc = g * math.sin(alfa) / (1 + Ik / (m * r ** 2))
eps = acc / r

px = [0, h / math.tan(alfa)]
py = [h, 0]
l = math.sqrt(h ** 2 + px[1] ** 2)


def stop(l):
    return len(l) == 33291


def Euler():
    l_ep = []
    l_ek = []
    l_ec = []
    l_t = []
    l_x = []
    l_y = []
    l_b = []

    t = 0
    sx = 0
    sy = r
    v = 0
    b = 0
    w = 0

    l_h = h

    while l_h > 0:
        dx = v * dt
        dv = acc * dt
        x = sx * math.cos(-alfa) - sy * math.sin(-alfa)
        y = sx * math.sin(-alfa) + sy * math.cos(-alfa) + h
        db = dt * w
        dw = dt * eps
        l_h = y - r

        l_x.append(x)
        l_y.append(y)
        l_b.append(b)

        ep = m * g * l_h
        ek = m * v ** 2 / 2 + Ik * w ** 2 / 2
        ec = ep + ek

        l_ep.append(ep)
        l_ek.append(ek)
        l_ec.append(ec)
        l_t.append(t)
        t += dt
        sx += dx
        v += dv
        b += db
        w += dw

    return l_ep, l_ek, l_ec, l_t, l_x, l_y, l_b


def ulepszony_Euler():
    l_ep = []
    l_ek = []
    l_ec = []
    l_t = []
    l_x = []
    l_y = []
    l_b = []

    t = 0
    sx = 0
    sy = r
    v = 0
    b = 0
    w = 0
    l_h = h

    while l_h > 0:
        v_u = v + g * dt / 2
        dx = v_u * dt
        dv = acc * dt
        x = sx * math.cos(-alfa) - sy * math.sin(-alfa)
        y = sx * math.sin(-alfa) + sy * math.cos(-alfa) + h

        b_u = b + w * dt / 2
        w_u = w + eps * dt / 2
        db = dt * w_u
        dw = dt * eps
        l_h = y - r

        l_x.append(x)
        l_y.append(y)
        l_b.append(b_u)

        ep = m * g * l_h
        ek = m * v_u ** 2 / 2 + Ik * w_u ** 2 / 2
        ec = ep + ek

        l_ep.append(ep)
        l_ek.append(ek)
        l_ec.append(ec)
        l_t.append(t)
        t += dt
        sx += dx
        v += dv
        b += db
        w += dw

    return l_ep, l_ek, l_ec, l_t, l_x, l_y, l_b


def Ep_vs_Ek_Ec(Ep, Ek, Ec, t):
    fig, ax = plt.subplots()
    ax.plot(t, Ep, label='Ep')
    ax.plot(t, Ek, label='Ek')
    ax.plot(t, Ec, label='Ec')
    ax.set_xlabel('Czas')
    ax.set_ylabel('Energia')
    ax.legend()

    plt.grid(True)
    plt.show()


def Ep_vs_Ek_Ec_v2(Ep1, Ek1, Ec1, Ep2, Ek2, Ec2, t):
    fig, ax = plt.subplots()
    ax.plot(t, Ep1, label='Ep1')
    ax.plot(t, Ek1, label='Ek1')
    ax.plot(t, Ec1, label='Ec1')

    ax.plot(t, Ep2, label='Ep2')
    ax.plot(t, Ek2, label='Ek2')
    ax.plot(t, Ec2, label='Ec2')
    ax.set_xlabel('Czas t [s]')
    ax.set_ylabel('Energia [J]')
    ax.legend()

    plt.grid(True)
    plt.show()


def polozenie(x, y):
    fig, ax = plt.subplots()
    ax.plot(px, py, label='rownia')
    ax.scatter(x, y, label='polozenie')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    plt.grid(True)
    plt.show()


# nie wiem jak, zrobie potem
def kat(t, b):
    fig, ax = plt.subplots()
    ax.plot(t, b, label='kat')

    ax.set_xlabel('Czas')
    ax.set_ylabel('Kat')
    ax.legend()

    plt.grid(True)
    plt.show()


ep2, ek2, ec2, t2, x2, y2, b2 = ulepszony_Euler()
#Ep_vs_Ek_Ec(ep2, ek2, ec2, t2)
polozenie(x2, y2)
#kat(t2, b2)

ep1, ek1, ec1, t1, x1, y1, b1 = Euler()
print("Euler:", abs(ec1[-1] - ec1[0]))
print("Ulepszony Euler:", abs(ec2[-1] - ec2[0]))

# print(len(ep2))
# print(len(ep1))
# Ep_vs_Ek_Ec_v2(ep1, ek1, ec1, ep2, ek2, ec2, t2)
# polozenie(x, y)
# kat(t, b)
# Ep_vs_Ek_Ec(ep1, ek1, ec1, t1)
