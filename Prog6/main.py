import math
from matplotlib import pyplot as plt

L = math.pi
n = 10
dx = L / n
dt = 0.3
mi = L / n
dl = 12


def Euler():
    list_i = list(range(n + 1))
    list_x = get_x_list(dx, n)
    list_f = []
    list_v = []
    list_a = []

    list_ep = []
    list_ek = []
    list_ec = []
    list_t = [0]

    for t in range(dl):
        list_fi = [0]
        list_vi = [0]
        list_ai = [0]
        list_ep.append(0)
        list_ek.append(0)

        if t == 0:
            for i in range(1, n):
                list_fi.append(math.sin(list_x[i]) / 1000)
                list_vi.append(0)
        else:
            for i in range(1, n):
                list_fi.append(list_f[t - 1][i] + list_v[t - 1][i] * dt)
                list_vi.append(list_v[t - 1][i] + list_a[t - 1][i] * dt)

        list_fi.append(0)
        list_vi.append(0)

        for i in range(1, n):
            list_ai.append((list_fi[i - 1] - 2 * list_fi[i] + list_fi[i + 1]) / (dx ** 2))

        list_ai.append(0)

        for e in range(n):
            list_ep[t] += (list_fi[e + 1] - list_fi[e]) ** 2

        for e in range(n):
            list_ek[t] += list_vi[e] ** 2

        list_ep[t] *= 1 / (2 * dx)
        list_ek[t] *= mi / 2
        list_ec.append(list_ep[t] + list_ek[t])

        list_f.append(list_fi)
        list_v.append(list_vi)
        list_a.append(list_ai)

    for e in range(dl - 1):
        list_t.append(list_t[e] + dt)

    print(list_ep, sep='\n')
    return list_f, list_i, list_ep, list_ek, list_ec, list_t


def ulepszony_Euler():
    list_i = list(range(n + 1))
    list_x = get_x_list(dx, n)
    list_f = []
    list_v = []
    list_a = []

    list_ep = []
    list_ek = []
    list_ec = []
    list_t = [0]

    for t in range(dl):
        list_fi = [0]
        list_vi = [0]
        list_ai = [0]
        list_ep.append(0)
        list_ek.append(0)

        if t == 0:
            for i in range(1, n):
                list_fi.append(math.sin(list_x[i]) / 1000)
                list_vi.append(0)
        else:
            for i in range(1, n):
                list_fi.append(list_f[t - 1][i] + list_v[t - 1][i] * dt)
                list_vi.append(list_v[t - 1][i] + list_a[t - 1][i] * dt)

        list_fi.append(0)
        list_vi.append(0)

        for i in range(1, n):
            list_ai.append((list_fi[i - 1] - 2 * list_fi[i] + list_fi[i + 1]) / (dx ** 2))

        list_ai.append(0)

        for e in range(n):
            list_ep[t] += (list_fi[e + 1] - list_fi[e]) ** 2

        for e in range(n):
            list_ek[t] += list_vi[e] ** 2

        list_ep[t] *= 1 / (2 * dx)
        list_ek[t] *= mi / 2
        list_ec.append(list_ep[t] + list_ek[t])

        list_f.append(list_fi)
        list_v.append(list_vi)
        list_a.append(list_ai)

    for e in range(dl - 1):
        list_t.append(list_t[e] + dt)

    print(list_ep, sep='\n')
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

    ax.set_xlim([0, t[len(t) - 1]])
    ax.set_ylim([0, 0.0000014])

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
