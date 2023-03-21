# przyjmuje wektory sil (listy ich) oddaje wektor sily wypadkowej
# policzyc jeszcze wypadkowo z sila osrodka (na razie bez)
def wypadkowa_sil(q, v, *args):
    fx = 0
    fy = 0
    for e in args:
        fx += e[0]
        fy += e[1]

    return [fx, fy]


def symulacja_Eurela(m, a, dt, t, s, v, ds, dv):
    x = []
    y = []
    while t <= 2.1:
        print(t, s, v, ds, dv)
        s[0] = round(ds[0] + s[0], 3)
        s[1] = round(ds[1] + s[1], 3)
        v[0] = round(dv[0] + v[0], 3)
        v[1] = round(dv[1] + v[1], 3)
        ds[0] = round(dt * v[0], 3)
        ds[1] = round(dt * v[1], 3)

        dv = [a[0] * dt, a[1] * dt]
        t = round(dt + t, 3)


def symulacja_ulepszona_Eurela(m, a, dt, t, s, v, ds, dv):
    new_v = [v[0] + (a[0] * dt) / 2, v[1] + (a[1] * dt) / 2]
    while t <= 2:
        a = wypadkowa_sil(0.1, [m * 0, m * 10])
        dv = [a[0] * dt, a[1] * dt]
        print(t, s, v, new_v, ds, dv)
        s[0] = round(ds[0] + s[0], 3)
        s[1] = round(ds[1] + s[1], 3)
        v[0] = round(dv[0] + v[0], 3)
        v[1] = round(dv[1] + v[1], 3)
        new_v = [v[0] + (a[0] * dt) / 2, v[1] + (a[1] * dt) / 2]
        ds[0] = dt * new_v[0]
        ds[1] = dt * new_v[1]

        t = round(dt + t, 3)


def main():
    m = 1
    q = 0.1
    g = [0, -10]
    dt = 0.1
    t = 0
    s = [0, 0]
    v = [10, 10]
    ds = [dt * v[0], dt * v[1]]
    dv = [g[0] * dt, g[1] * dt]

    fw = wypadkowa_sil(q, 1, [m * g[0], m * g[1]])
    a = [fw[0] / m, fw[1] / m]
    # symulacja_Eurela(m, a, dt, t, s, v, ds, dv)
    symulacja_ulepszona_Eurela(m, a, dt, t, s, v, ds, dv)


main()
# while t <= 2.1:
# print(t, Sx, Sy, Vx, Vy, DSx, DSy, DVx, DVy, sep="        ")
# t = round(t + dt, 2)
# Sx = round(DSx + Sx, 2)
# Sy = round(DSy + Sy, 2)
# DSx = round(Vx * dt + DSx, 2)
# DSy -= 0.1
# Vx = round(DVx + Vx, 2)
# Vy = round(DVy + Vy, 2)

# Eurel
# Ruch x i y oddzielnie
