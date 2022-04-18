#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator
"""
Реализовать класс Money, используя для представления денег список словарей.
Словарь имеет два ключа: номинал купюры и количество купюр данного достоинства.
Номиналы представить как строку. Элемент списка словарей с меньшим индексом
содержит меньший номинал.
"""


class Money:

    def __init__(self, *bills):
        self.bills = [*bills]  # Список всех купюр
        self.count = sum([bill['number'] for bill in self.bills])
        self.__size = 10  # Максимально допустимое количество купюр

    @property
    def size(self):
        return self.__size

    def __add__(self, bill):
        if self.count + bill['number'] <= self.size:
            bills = self.bills
            bills.append(bill)
            new = []
            for i, bill in enumerate(bills):
                sov = 0  # Прибавляемое число при совпадении
                for next in bills[i+1:]:
                    if next['denominator'] == bill['denominator']:
                        sov += next['number']
                        del bills[i+1]
                bill['number'] += sov
                new.append(bill)
            self.bills = new
            self.__sorting()
        else:
            print("Кошелёк не вмещает столько купюр")
        return self

    def __sub__(self, other):
        bills = self.bills
        for bill in bills:
            if other['denominator'] == bill['denominator']:
                bill['number'] -= other['number']
                if bill['number'] <= 0:
                    bills.remove(bill)
        self.bills = bills
        self.__sorting()
        return self

    def display(self):
        print("Купюры в кошельке:")
        for bill in self.bills:
            print(f"Купюра номиналом - {bill['denominator']}. "
                  f"Количество этих купюр - {bill['number']}")

    def __sorting(self):
        cons = {'one': 1, 'two': 2, 'five': 5, 'ten': 10, 'fifty': 50,
                'hundred': 100, 'five hundred': 500, 'thousand': 1000,
                'five thousand': 5000}
        # Замена строковых значений 'denominator' на числа
        # и добавление их в новых словарь new
        new = []
        for bill in self.bills:
            for key, value in cons.items():
                if bill['denominator'] == key:
                    bill['denominator'] = value
            new.append(bill)
        # Сортировка
        new.sort(key=operator.itemgetter('denominator'))
        # Обратная замена 'denominator' на строковые значения
        for bill in new:
            for key, value in cons.items():
                if bill['denominator'] == value:
                    bill['denominator'] = key
        self.bills = new


if __name__ == "__main__":
    # Две пачки купюр
    a = {'denominator': "fifty", 'number': 3}
    b = {'denominator': "hundred", 'number': 1}

    print("\n### Создание  ###")  # Кошелька из двух пачек
    A = Money(a, b)
    A.display()
    print("\n### Сумма ###")  # Кошелька и пачки b
    A = A + b
    A.display()
    print("\n### Разность ###")  # Кошелька и пачки b
    A = A - b
    A.display()
