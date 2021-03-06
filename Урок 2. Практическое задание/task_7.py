"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum(num):
    if num == 0:
        return num
    else:
        return num + sum(num - 1)


try:
    num = int(input(f'введите целое число: '))
    if sum(num) == num * (num + 1) / 2:
        print(f'{sum(num)} = {int(num * (num + 1) / 2)} доказано!')
    else:
        print(f'где-то затаилась ошибка...')
except ValueError:
    print(f'введите все-таки число...')
