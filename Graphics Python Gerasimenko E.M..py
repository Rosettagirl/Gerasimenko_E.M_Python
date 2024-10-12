print("Упражнение №2:")
import numpy as np
import matplotlib.pyplot as plt
def y(x):
    return x**2 - x - 6
x = np.linspace(-10, 10, 100)
y_values = y(x)
plt.figure(figsize=(8,6))
plt.plot(x, y_values, label='y(x) = x^2 - x - 6')
plt.axhline(y=0, color='y', linestyle='--') # ось x
plt.axvline(x=0, color='y', linestyle='--') # ось y
plt.axvline(x=3, color='g', linestyle='--') # корень уравнения
plt.axvline(x=-2, color='g', linestyle='--') # корень уравнения
plt.title('График функции y(x) = x^2 - x - 6')
plt.legend()
plt.grid(True)
plt.show()


print("Упражнение №3:")
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.log1p(np.tan(1 / (1 + np.sin(x)**2))) * (x**2 + 1) * np.exp(-np.abs(x) / 10)
x = np.linspace(-20, 20, 400)
y = f(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\log_{1+\tan{\left(\frac{1}{1+\sin^2{x}}\right)}}(x^2 + 1)\exp{\left(-\frac{|x|}{10}\right)}$', color='blue')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

print('Упражнение №5:')
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Генерация данных
np.random.seed(0)  # Для воспроизводимости
x = np.linspace(0, 10, 10)  # 10 равномерно распределенных точек
true_function = 2 * x + 1  # Истинная функция (линейная)
noise = np.random.normal(0, 2, size=x.shape)  # Погрешность
y = true_function + noise  # Наблюдаемые данные с погрешностью

# Аппроксимация многочленом первой степени (линейная регрессия)
coeffs_linear = np.polyfit(x, y, 1)  # Коэффициенты линейного многочлена
linear_poly = np.poly1d(coeffs_linear)

# Аппроксимация многочленом второй степени
coeffs_quadratic = np.polyfit(x, y, 2)  # Коэффициенты второго многочлена
quadratic_poly = np.poly1d(coeffs_quadratic)

# Генерация новых значений для построения гладкой аппроксимации
x_new = np.linspace(0, 10, 100)
y_linear = linear_poly(x_new)
y_quadratic = quadratic_poly(x_new)

# Визуализация
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Данные с погрешностями')
plt.errorbar(x, y, yerr=2, fmt='o', color='red', label='Погрешности', capsize=5)
plt.plot(x_new, y_linear, label='Аппроксимация 1-й степени', color='blue')
plt.plot(x_new, y_quadratic, label='Аппроксимация 2-й степени', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Аппроксимация данных многочленами')
plt.legend()
plt.grid()
plt.show()


print("Упражнение №6:")
x_data = np.arange(-2, 2.01, 0.001)
n = 100
b = 0.5
a = 3
y_data = np.array([])
y = np.array([])
for x in x_data:
    for i in range(n):
        y = np.append(y, np.cos(np.pi * x * a ** i) * b ** i)
    y_sum = np.sum(y)
    y_data = np.append(y_data, y_sum)
    y = np.array([])
plt.plot(x_data, y_data)
plt.title('Функция Вейерштрасса')
plt.axis('equal')
plt.grid = True
plt.show()


print("Упражнение №4:")
plt.xkcd()
user_input = input("Введите функцию переменной x (например, np.sin(x), x**2, np.exp(x)): ")
x = np.linspace(-10, 10, 400)
try:
    y = eval(user_input)
except Exception as e:
    print(f"Произошла ошибка при вычислении функции: {e}")
    exit()
plt.plot(x, y, label=f'y = {user_input}')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.show()