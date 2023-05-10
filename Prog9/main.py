import matplotlib.pyplot as plt

A = 10
B = 25
C = 8 / 3
# dt = 0.03
dt = 0.028347
max_t = 3000

x0, y0, z0 = 1, 1, 1


def dx_dt(x, y):
    return A * y - A * x


def dy_dt(x, y, z):
    return -x * z + B * x - y


def dz_dt(x, y, z):
    return x * y - C * z


def euler():
    x = [x0]
    y = [y0]
    z = [z0]

    for i in range(max_t - 1):
        x.append(x[i] + dt * dx_dt(x[i], y[i]))
        y.append(y[i] + dt * dy_dt(x[i], y[i], z[i]))
        z.append(z[i] + dt * dz_dt(x[i], y[i], z[i]))

    return x, z


def midpoint():
    x = [x0]
    y = [y0]
    z = [z0]

    for i in range(max_t):
        x_mid = x[i] + 0.5 * dt * dx_dt(x[i], y[i])
        y_mid = y[i] + 0.5 * dt * dy_dt(x[i], y[i], z[i])
        z_mid = z[i] + 0.5 * dt * dz_dt(x[i], y[i], z[i])

        x.append(x[i] + dt * dx_dt(x_mid, y_mid))
        y.append(y[i] + dt * dy_dt(x_mid, y_mid, z_mid))
        z.append(z[i] + dt * dz_dt(x_mid, y_mid, z_mid))

    return x, z


def rk4():
    x = [x0]
    y = [y0]
    z = [z0]

    for i in range(max_t):
        k1_x = dt * dx_dt(x[i], y[i])
        k1_y = dt * dy_dt(x[i], y[i], z[i])
        k1_z = dt * dz_dt(x[i], y[i], z[i])

        k2_x = dt * dx_dt(x[i] + 0.5 * k1_x, y[i] + 0.5 * k1_y)
        k2_y = dt * dy_dt(x[i] + 0.5 * k1_x, y[i] + 0.5 * k1_y, z[i] + 0.5 * k1_z)
        k2_z = dt * dz_dt(x[i] + 0.5 * k1_x, y[i] + 0.5 * k1_y, z[i] + 0.5 * k1_z)

        k3_x = dt * dx_dt(x[i] + 0.5 * k2_x, y[i] + 0.5 * k2_y)
        k3_y = dt * dy_dt(x[i] + 0.5 * k2_x, y[i] + 0.5 * k2_y, z[i] + 0.5 * k2_z)
        k3_z = dt * dz_dt(x[i] + 0.5 * k2_x, y[i] + 0.5 * k2_y, z[i] + 0.5 * k2_z)

        k4_x = dt * dx_dt(x[i] + k3_x, y[i] + k3_y)
        k4_y = dt * dy_dt(x[i] + k3_x, y[i] + k3_y, z[i] + k3_z)
        k4_z = dt * dz_dt(x[i] + k3_x, y[i] + k3_y, z[i] + k3_z)

        x.append(x[i] + (1 / 6) * (k1_x + 2 * k2_x + 2 * k3_x + k4_x))
        y.append(y[i] + (1 / 6) * (k1_y + 2 * k2_y + 2 * k3_y + k4_y))
        z.append(z[i] + (1 / 6) * (k1_z + 2 * k2_z + 2 * k3_z + k4_z))

    return x, z


def show(x, z):
    plt.plot(x, z, label='CHART')
    plt.xlabel('x')
    plt.ylabel('t')
    plt.grid()
    plt.legend()
    plt.show()


x_euler, z_euler = euler()

x_midpoint, z_midpoint = midpoint()

x_rk4, z_rk4 = rk4()

show(x_euler, z_euler)
show(x_midpoint, z_midpoint)
show(x_rk4, z_rk4)
