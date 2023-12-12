#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = int(input("Введите номер месяца:"))
    if m < 1 or m > 12:
        print("Месяца с таким числом не существует")
        exit(1)
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        days_number = 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        days_number = 30
    else:
        days_number = 28
    print("В этом месяце", days_number, "дней")
