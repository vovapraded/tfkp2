import numpy as np
import matplotlib.pyplot as plt

def transform_cosh(z):
    return np.cosh(z)

def branch_sqrt(z):
    root = np.sqrt(z)
    return np.where(np.imag(root) >= 0, root, -root)

def second_transform(w):
    return -w + branch_sqrt(w**2 - 1)

# --- Визуализация с сохранением ---
def plot_complex_points(Z, title, filename, color='blue', size=0.5):
    plt.figure(figsize=(8, 6))
    plt.scatter(Z.real, Z.imag, color=color, s=size)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid(True)
    plt.axis('equal')
    plt.savefig(filename)  # Сохраняем изображение в файл
    plt.close()  # Закрываем изображение, чтобы не мешало при создании следующего

# --- Генерация сетки комплексных чисел ---
def generate_initial_grid():
    x = np.linspace(0.000001, 10, 500)  # Реальная часть
    y = np.linspace(0.000001, np.pi - 0.000000001, 400)  # Мнимая часть
    X, Y = np.meshgrid(x, y)
    return X + 1j * Y

# Генерируем начальное множество
Z = generate_initial_grid()

# Шаг 1: Визуализация начального множества
plot_complex_points(Z, 'Исходное множество: 0 < Im(z) < pi, Re(z) > 0', 'task2.1.png', color='blue')

# Применяем первое преобразование (cosh)
W1 = transform_cosh(Z)
plot_complex_points(W1, 'После первого преобразования: w = cosh(z)', 'task2.2.png', color='green')

# Применяем второе преобразование: f(w) = -w + sqrt(w^2 - 1)
W2 = second_transform(W1)
plot_complex_points(W2, 'После второго преобразования: f(w) = -w + sqrt(w^2 - 1)', 'task2.3.png', color='red')