#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    number_n = int(input("Введите число n:"))
    number_k = int(input("Введите число k:"))
    if number_n < 1 or number_n > 4:
        print("n не удовлетворяет условиям 1<n<4")
        exit(1)
    sum_k = 0
    for i in range(10**(number_n-1), 10**number_n):
        if i % number_k == 0:
            sum_k += i
        i += 1
    print("Сумма", number_n, "значных чисел =", sum_k)
