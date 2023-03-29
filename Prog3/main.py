from matplotlib import pyplot as plt
import math

m = 1
g = -9.81
dt = 0.1
l = 1
t = 0
t_max = 13
alfa = math.radians(45)
omega = 0


def symulacja_Eulera(m, g, dt, l, t, alfa, omega):
    wyniki_t = []
    wyniki_x = []
    wyniki_y = []
    wyniki_alfa = []
    wyniki_omega = []
    wyniki_Ep = []
    wyniki_Ek = []
    wyniki_Ec = []

    while t <= t_max:
        eps = g / l * math.sin(alfa)
        da = omega * dt
        dw = eps * dt
        x = l * math.cos(alfa - math.radians(90))
        y = l * math.sin(alfa - math.radians(90))

        h = l + y
        v = l * omega
        Ep = abs(m * g * h)
        Ek = m * v ** 2 / 2
        Ec = Ep + Ek
        wyniki_t.append(t)
        wyniki_x.append(x)
        wyniki_y.append(y)
        wyniki_alfa.append(alfa)
        wyniki_omega.append(omega)
        wyniki_Ep.append(Ep)
        wyniki_Ek.append(Ek)
        wyniki_Ec.append(Ec)

        t += dt
        alfa += da
        omega += dw

    return wyniki_t, wyniki_alfa, wyniki_omega, wyniki_x, wyniki_y, wyniki_Ep, wyniki_Ek, wyniki_Ec


def symulacja_ulepszona_Eulera(m, g, dt, l, t, alfa, omega):
    wyniki_t = []
    wyniki_x = []
    wyniki_y = []
    wyniki_alfa = []
    wyniki_omega = []
    wyniki_Ep = []
    wyniki_Ek = []
    wyniki_Ec = []

    while t <= t_max:
        eps = g / l * math.sin(alfa)
        alfa_p = alfa + omega * dt / 2
        omega_p = omega + eps * dt / 2
        eps_p = g / l * math.sin(alfa_p)
        da = omega_p * dt
        dw = eps_p * dt
        alfa = alfa + da
        omega = omega + dw
        x = l * math.cos(alfa - math.radians(90))
        y = l * math.sin(alfa - math.radians(90))

        h = l + y
        v = l * omega
        Ep = abs(m * g * h)
        Ek = m * v ** 2 / 2
        Ec = Ep + Ek

        wyniki_t.append(t)
        wyniki_x.append(x)
        wyniki_y.append(y)
        wyniki_alfa.append(alfa)
        wyniki_omega.append(omega)
        wyniki_Ep.append(Ep)
        wyniki_Ek.append(Ek)
        wyniki_Ec.append(Ec)

        t += dt

    return wyniki_t, wyniki_alfa, wyniki_omega, wyniki_x, wyniki_y, wyniki_Ep, wyniki_Ek, wyniki_Ec


def symulacja_rk4(m, g, dt, l, t, alfa, omega):
    wyniki_t = []
    wyniki_x = []
    wyniki_y = []
    wyniki_alfa = []
    wyniki_omega = []
    wyniki_Ep = []
    wyniki_Ek = []
    wyniki_Ec = []

    while t <= t_max:
        k1a = omega
        k1w = g / l * math.sin(alfa)

        k2a = omega + dt / 2 * k1w
        k2w = g / l * math.sin(alfa + dt / 2 * k1a)

        k3a = omega + dt / 2 * k2w
        k3w = g / l * math.sin(alfa + dt / 2 * k2a)

        k4a = omega + dt * k3w
        k4w = g / l * math.sin(alfa + dt * k3a)

        da = dt / 6 * (k1a + 2 * k2a + 2 * k3a + k4a)
        dw = dt / 6 * (k1w + 2 * k2w + 2 * k3w + k4w)

        alfa += da
        omega += dw

        x = l * math.cos(alfa - math.radians(90))
        y = l * math.sin(alfa - math.radians(90))

        h = l + y
        v = l * omega
        Ep = abs(m * g * h)
        Ek = m * v ** 2 / 2
        Ec = Ep + Ek

        wyniki_t.append(t)
        wyniki_x.append(x)
        wyniki_y.append(y)
        wyniki_alfa.append(alfa)
        wyniki_omega.append(omega)
        wyniki_Ep.append(Ep)
        wyniki_Ek.append(Ek)
        wyniki_Ec.append(Ec)

        t += dt

    return wyniki_t, wyniki_alfa, wyniki_omega, wyniki_x, wyniki_y, wyniki_Ep, wyniki_Ek, wyniki_Ec


def Ep_vs_Ek_Ec(Ep, Ek, Ec, t):
    fig, ax = plt.subplots()
    ax.plot(t, Ep, label='Ep')
    ax.plot(t, Ek, label='Ek')
    ax.plot(t, Ec, label='Ec')
    ax.set_xlabel('Czas t [s]')
    ax.set_ylabel('Energia [J]')
    ax.legend()

    plt.grid(True)
    plt.show()


def omega_display(alfa, omega):
    fig, ax = plt.subplots()
    ax.plot(alfa, omega, label='Omega')
    ax.legend()

    plt.grid(True)
    plt.show()


def Ec_display(Ec):
    fig, ax = plt.subplots()
    ax.plot(Ec, label='Ec')
    ax.legend()
    ax.set_ylabel('Energia [J]')

    plt.grid(True)
    plt.show()


def trajektoria(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Trajektoria')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.ylim(min(y) - 0.2, 0)

    plt.grid(True)
    plt.show()


#n_t, n_alfa, n_omega, x, y, Ep, Ek, Ec = symulacja_Eulera(m, g, dt, l, t, alfa, omega)
#Ep_vs_Ek_Ec(Ep, Ek, Ec, n_t)
#omega_display(n_alfa, n_omega)
#Ec_display(Ec)
#trajektoria(x, y)
#
#n_t, n_alfa, n_omega, x, y, Ep, Ek, Ec = symulacja_ulepszona_Eulera(m, g, dt, l, t, alfa, omega)
#Ep_vs_Ek_Ec(Ep, Ek, Ec, n_t)
#omega_display(n_alfa, n_omega)
#Ec_display(Ec)
#trajektoria(x, y)

n_t, n_alfa, n_omega, x, y, Ep, Ek, Ec = symulacja_rk4(m, g, dt, l, t, alfa, omega)
Ep_vs_Ek_Ec(Ep, Ek, Ec, n_t)
omega_display(n_alfa, n_omega)
Ec_display(Ec)
trajektoria(x, y)
