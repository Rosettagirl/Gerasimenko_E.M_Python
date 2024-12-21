# Лаб. работа №3
# Герасименко Екатерина, 100502-УБТа-о23, Вариант 6

import math as m

x1 = 2
xn = 5
dx = 0.5
a = 1.5
b = 4.8

# С помощью цикла for
per = int((xn - x1) / dx + 1)

results = []

for x in range(per):
    x = x1 + x * dx
    y = a * (b/x - (m.log(a*x) / b**2))
    results.append((x, y))

for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")

# С помощью цикла While
x = x1
while x <= xn:
    y = a * (b/x - (m.log(a*x) / b**2))
    results.append((x, y))
    x += dx

for x, y in results:
    print(f"x = {x:.1f}, y = {y:.4f}")
