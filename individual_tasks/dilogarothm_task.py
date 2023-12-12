#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# Точность вычислений.
EPS = 1e-10


if __name__ == '__main__':
    x = float(input("Введите аргумент x (0 <= x <= 2): "))
    if x < 0 or x > 2:
        print("Аргумент не подходит заданным условиям", file=sys.stderr)
        exit(1)

    a = 1 - x    # Первый член ряда
    sum_row = a  # Сумма членов ряда
    k = 1        # Счетчик
    # Найдем сумму членов ряда.
    while math.fabs(a) > EPS:
        a *= ((1 - x) * (k**2)) / ((k + 1)**2)
        sum_row += a
        k += 1
    # Вывести значение функции.
    print("Значение функции (дилогарифма) =", sum_row)
