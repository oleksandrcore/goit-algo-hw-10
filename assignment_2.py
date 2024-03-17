import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


def monte_carlo_integration(f, a, b, num_points):
    x = np.random.uniform(a, b, num_points)
    y = f(x)
    
    mean_value = np.mean(y)
    rect_area = (b - a) * np.max(y)
    integral_value = mean_value * (b - a)
    
    return integral_value

num_points = 100000
integral_value = monte_carlo_integration(f, a, b, num_points)
print("Значення інтеграла, обчислене методом Монте-Карло з 100000 точками:", integral_value)
num_points = 1000
integral_value = monte_carlo_integration(f, a, b, num_points)
print("Значення інтеграла, обчислене методом Монте-Карло з 1000 точками:", integral_value)


result, error = spi.quad(f, a, b)
print("Інтеграл: ", result)
