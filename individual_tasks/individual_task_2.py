#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорт модуля, который позволяет вычислить корни отрицательных чисел
import cmath
import math

if __name__ == '__main__':
    coef_a = float(input("Введите коэффициент a: "))
    coef_b = float(input("Введите коэффициент b: "))
    coef_c = float(input("Введите коэффициент c: "))
    # Вычисление дискриминанта
    discriminant = (coef_b ** 2) - (4 * coef_a * coef_c)
    # Вычисление корней квадратного уравнения в зависимости от дискриминанта
    if discriminant > 0:
        root_1 = (-coef_b + math.sqrt(discriminant)) / (2 * coef_a)
        root_2 = (-coef_b - math.sqrt(discriminant)) / (2 * coef_a)
    elif discriminant == 0:
        root_1 = -coef_b / (2 * coef_a)
        root_2 = -coef_b / (2 * coef_a)
    else:
        root_1 = (-coef_b + cmath.sqrt(discriminant)) / (2 * coef_a)
        root_2 = (-coef_b - cmath.sqrt(discriminant)) / (2 * coef_a)
    # Вывод результатов в зависимости от видов корней
    if discriminant > 0:
        print("Уравнение имеет два корня:")
        print("Корень x1 =", root_1)
        print("Корень x2 =", root_2)
    elif discriminant == 0:
        print("Уравнение имеет один корень:")
        print("Корень x =", root_1)
    else:
        print("Уравнение имеет два комплексных корня:")
        print("Корень W1 =", root_1)
        print("Корень W2 =", root_2)
