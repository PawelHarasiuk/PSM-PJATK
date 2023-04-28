import math

from matplotlib import pyplot as plt

L = math.pi
n = 10
dx = L / n
dt = 0.1
mi = L / n
dl = 30


def Euler():
    list_i = list(range(n + 1))
    list_x = get_x_list(dx, n)

    list_f = []
    list_v = []
    list_a = []

    list_f2 = []
    list_v2 = []
    list_a2 = []

    list_ep = []
    list_ek = []
    list_ec = []
    list_t = [0]

    for t in range(dl):
        list_fi = [0]
        list_vi = [0]
        list_ai = [0]

        list_fi2 = [0]
        list_vi2 = [0]
        list_ai2 = [0]

        list_ep.append(0)
        list_ek.append(0)

        if t == 0:
            for i in range(1, n):
                list_fi.append(math.sin(list_x[i]))
                list_vi.append(0)
        else:
            for i in range(1, n):
                list_fi.append(list_f[t - 1][i] + list_v2[t - 1][i] * dt)
                list_vi.append(list_v[t - 1][i] + list_a2[t - 1][i] * dt)

        list_fi.append(0)
        list_vi.append(0)

        for i in range(1, n):
            list_ai.append((list_fi[i - 1] - 2 * list_fi[i] + list_fi[i + 1]) / (dx ** 2))

        list_ai.append(0)

        for i in range(1, n):
            list_fi2.append(list_fi[i] + (list_vi[i] * dt) / 2)
            list_vi2.append(list_vi[i] + (list_ai[i] * dt) / 2)

        list_fi2.append(0)
        list_vi2.append(0)

        for i in range(1, n):
            list_ai2.append((list_fi2[i - 1] - 2 * list_fi2[i] + list_fi2[i + 1]) / (dx ** 2))

        list_ai2.append(0)

        for e in range(n):
            list_ep[t] += (list_fi2[e + 1] - list_fi2[e]) ** 2

        for e in range(n):
            list_ek[t] += list_vi2[e] ** 2

        list_ep[t] *= 1 / (2 * dx)
        list_ek[t] *= mi / 2
        list_ec.append(list_ep[t] + list_ek[t])

        list_f.append(list_fi)
        list_v.append(list_vi)
        list_a.append(list_ai)

        list_f2.append(list_fi2)
        list_v2.append(list_vi2)
        list_a2.append(list_ai2)

    for e in range(dl - 1):
        list_t.append(list_t[e] + dt)

    return list_f, list_i, list_ep, list_ek, list_ec, list_t


def polozenie(f, i):
    fig, ax = plt.subplots()

    for e in range(len(f)):
        ax.plot(i, f[e])

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.grid(True)
    plt.show()


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


def get_x_list(dx, n):
    x = [0]
    for i in range(n):
        x.append(x[i] + dx)

    return x


if __name__ == "__main__":
    f, i, ep, ek, ec, t = Euler()

    Ep_vs_Ek_Ec(ep, ek, ec, t)
    polozenie(f, i)
