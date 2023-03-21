import numpy as np
import matplotlib.pyplot as plt


def wypadkowa_sila(F):
    """Oblicza wypadkową siłę na podstawie sił działających na punkt materialny."""
    F_x = np.sum([f[0] for f in F])
    F_y = np.sum([f[1] for f in F])
    return np.array([F_x, F_y])


def symulacja_Eulera(q, dt, t_max, m, s_0, v_0):
    t = np.arange(0, t_max, dt)
    s = np.zeros((len(t), 2))
    v = np.zeros((len(t), 2))

    # Warunki początkowe
    s[0] = s_0
    v[0] = v_0

    for i in range(len(t) - 1):
        # Obliczenie sił wypadkowych
        F_wypadkowa = np.array([0, -m * 9.81]) - q * v[i]

        # Obliczenie przyspieszenia
        a = F_wypadkowa / m

        # Obliczenie prędkości i położenia w następnym kroku czasowym
        v[i + 1] = v[i] + a * dt
        s[i + 1] = s[i] + v[i + 1] * dt

    return s


def symulacja_ulepszona_Eulera(q, dt, t_max, m, s_0, v_0):
    """Symuluje ruch punktu materialnego zgodnie z układem równań ulepszoną metodą Eulera."""
    # Liczba kroków czasowych
    n = int(t_max / dt)

    # Inicjalizacja tablic przechowujących trajektorię punktu materialnego
    s = np.zeros((n + 1, 2))
    v = np.zeros((n + 1, 2))

    # Warunki początkowe
    s[0] = s_0
    v[0] = v_0

    # Symulacja ruchu
    for i in range(n):
        # Obliczenie siły oporu w połowie przedziału czasowego
        v_half = v[i] + 0.5 * wypadkowa_sila([-q * v[i]]) / m * dt
        F_opor = -q * v_half
        # Obliczenie wypadkowej siły
        F_wypadkowa = wypadkowa_sila([F_opor])

        # Obliczenie prędkości i położenia
        # Obliczenie przyspieszenia
        a = F_wypadkowa / m

        # Obliczenie prędkości i położenia w następnym kroku czasowym
        v[i + 1] = v_half + 0.5 * a * dt
        s[i + 1] = s[i] + v[i + 1] * dt

    return s


def main():
    # Parametry symulacji
    q = 0.5
    dt = 0.1
    t_max = 21
    m = 10
    s_0 = np.array([0, 0])
    v_0 = np.array([10, 10])

    # Symulacja ruchu metodą Eulera
    s_euler = symulacja_Eulera(q, dt, t_max, m, s_0, v_0)

    # Symulacja ruchu ulepszoną metodą Eulera
    s_ulepszona_euler = symulacja_ulepszona_Eulera(q, dt, t_max, m, s_0, v_0)

    # Wykres trajektorii punktu materialnego
    plt.plot(np.arange(0, t_max, dt), s_euler[:, 1])
    # plt.plot(s_ulepszona_euler[:, 0], s_ulepszona_euler[:, 1], label='Ulepszona metoda Eulera')
    plt.figure(figsize=(8, 6))
    plt.xlim([0, t_max])
    plt.ylim([0, None])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show()


main()

