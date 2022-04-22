#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1,
максимально задействовав имеющиеся средства перегрузки операторов.
"""


class Interval:

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def __contains__(self, item):
        if first <= num <= second:
            return True
        else:
            return False

    def display(self):
        print(f"Интервал начинается с {self.first} и до {self.second}")


if __name__ == '__main__':

    while True:
        # Создание интервала
        first = int(input("\nВведите левую границу интервала: "))
        second = int(input("Введите правую границу интервала: "))
        a = Interval(first, second)
        a.display()

        # Проверка нахождения числа в интервале
        num = int(input("Введите число: "))
        if num in a:
            print("Число присутствует в интервале")
        else:
            print("Число отсутсвует в интервале")
