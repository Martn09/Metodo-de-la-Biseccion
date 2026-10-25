import numpy as np
import matplotlib.pyplot as plt


def biseccion(f, a, b, tol, n0):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None

    i = 1
    while i <= n0:
        p = a + (b - a) / 2.0
        fp = f(p)
        if fp == 0 or (b - a) / 2.0 < tol:
            return p

        i += 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
    print(f"El método fracasó después de {n0} iteraciones")
    return None


x = np.linspace(0, 5, 1000)
y1 = x
y2 = np.tan(x)
tol_asintota = 10
y2[np.abs(y2) > tol_asintota] = np.nan

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='$y = x$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$y = \tan(x)$', color='red', linewidth=2)

raiz_x = biseccion(lambda x: x - np.tan(x), 4, 4.5, 1e-6, 100)
raiz_y = raiz_x
plt.scatter([raiz_x], [raiz_y], color='green', zorder=5)
plt.annotate(f'Solución ($x \\approx {raiz_x:.4f}$)',
             xy=(raiz_x, raiz_y),
             xytext=(raiz_x - 1.5, raiz_y + 2),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.ylim(-10, 10)
plt.xlim(0, 5)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title(r'Intersección de $y = x$ y $y = \tan(x)$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()