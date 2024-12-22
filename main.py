import numpy as np
import matplotlib.pyplot as plt

# --- Этап 1: Создаем начальное множество (полукруг) ---
def generate_initial_points():
    theta = np.linspace(0.01, np.pi - 0.01, 300)  # Угол от 0 до pi
    r = np.linspace(0.01, 0.99, 3000)  # Радиусы смещаем ближе к 1
    R, T = np.meshgrid(r, theta)
    X = R * np.cos(T)  # Действительная часть
    Y = R * np.sin(T)  # Мнимая часть
    return X + 1j * Y  # Комплексное число

# --- Этап 2: Функция f(z) ---
def f(z):
    return np.acosh(-0.5 * (z + 1 / z))

# --- Этап 3: Визуализация множества ---
def plot_complex_points(Z, title, color='blue', size=0.5):
    plt.figure(figsize=(8, 6))
    plt.scatter(Z.real, Z.imag, color=color, s=size)
    plt.title(title)
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# --- Этап 4: Преобразование и визуализация по этапам ---
# Генерируем начальное множество
Z_initial = generate_initial_points()

# Шаг 1: Визуализация начального множества
plot_complex_points(Z_initial, 'Начальное множество: Полукруг |z| < 1, Im(z) > 0')

# Шаг 2: Применяем первое преобразование: w = -0.5 * (z + 1/z)
W1 = -0.5 * (Z_initial + 1 / Z_initial)
plot_complex_points(W1, 'После первого преобразования: w = -0.5 * (z + 1/z)', color='green')

# Шаг 3: Применяем второе преобразование: w = acosh(w)
W2 = np.acosh(W1)
plot_complex_points(W2, 'После второго преобразования: w = acosh(-0.5 * (z + 1/z))', color='red')