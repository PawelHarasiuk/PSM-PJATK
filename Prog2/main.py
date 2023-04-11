from matplotlib import pyplot as plt


def wypadkowa_sil(q, v, g, m, *args):
    fx = m * g[0]
    fy = m * g[1]

    fx -= q * v[0]
    fy -= q * v[1]

    for f in args:
        fx += f[0]
        fy += f[1]

    return [fx, fy]


def symulacja_Eurela(m, q, g, dt, max_t, s, v, *args):
    ds = [dt * v[0], dt * v[1]]
    dv = [g[0] * dt, g[1] * dt]
    t = 0

    x = []
    y = []
    while max_t >= t:
        x.append(s[0])
        y.append(s[1])
        f = wypadkowa_sil(q, v, g, m, *args)
        a = [f[0] / m, f[1] / m]
        s[0] = ds[0] + s[0]
        s[1] = ds[1] + s[1]
        v[0] = dv[0] + v[0]
        v[1] = dv[1] + v[1]
        ds[0] = dt * v[0]
        ds[1] = dt * v[1]

        dv = [a[0] * dt, a[1] * dt]
        t = round(dt + t, 3)

    return x, y


def symulacja_ulepszona_Eurela(m, q, g, dt, max_t, s, v, *args):
    ds = [dt * v[0], dt * v[1]]
    dv = [g[0] * dt, g[1] * dt]
    t = 0

    x = []
    y = []
    while max_t >= t:
        x.append(s[0])
        y.append(s[1])
        f = wypadkowa_sil(q, v, g, m, *args)
        a = [f[0] / m, f[1] / m]
        s[0] = ds[0] + s[0]
        s[1] = ds[1] + s[1]
        v[0] = dv[0] + v[0]
        v[1] = dv[1] + v[1]
        new_v = [v[0] + (a[0] * dt) / 2, v[1] + (a[1] * dt) / 2]
        ds[0] = dt * new_v[0]
        ds[1] = dt * new_v[1]

        dv = [a[0] * dt, a[1] * dt]
        t = round(dt + t, 3)

    return x, y


def main():
    m = 1
    dt = 0.1
    max_t = 2.5
    q = 0.1
    gx = 0
    gy = -10
    sx = 0
    sy = 10
    vx = 10
    vy = 0

    x1, y1 = symulacja_Eurela(m, q, [gx, gy], dt, max_t, [sx, sy], [vx, vy])
    x2, y2 = symulacja_ulepszona_Eurela(m, q, [gx, gy], dt, max_t, [sx, sy], [vx, vy])

    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Euler Simulation')
    plt.xlim(0, max(x1))
    plt.ylim(0, max(y1))
    plt.xticks(range(0, int(max(x1)) + 2, 1))
    plt.yticks(range(0, int(max(y1)) + 2, 1))
    plt.plot(x1, y1, label="Eurel")
    plt.plot(x2, y2, label="Ulepszony Eurel")
    plt.legend()

    plt.grid(True)
    plt.show()


main()

