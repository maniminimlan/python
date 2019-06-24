
__author__ = 'Манинец Анатолий Андреевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print('-----------------------------')
print("Search max number")
print('-----------------------------')
number = 56465469710
print(number)

str_number = str(number)

len_number_origin = len(str_number)
len_number = len_number_origin

print('-----------------------------')
print("Loop 'while'")
print('-----------------------------')
max_number = 0
while len_number > 0:
    len_number -= 1
    number = int(str_number[len_number])
    len_number2 = len_number_origin
    if number > max_number:
        while len_number2 > 0:
            len_number2 -= 1
            number2 = int(str_number[len_number2])
            if number > number2:
                max_number = number
                print("{} больше {}".format(number, number2))
            elif number == number2:
                print("{} равно {}".format(number, number2))
            else:
                max_number = number2
                print("{} меньше {}".format(number, number2))
print("Максимальная цифра: {}".format(max_number))


print('-----------------------------')
print("Loop 'for'")
print('-----------------------------')
max_number2 = 0
for number in str_number:
    int_number = int(number)
    if int_number > max_number2:
        for number2 in str_number:
            int_number2 = int(number2)
            if int_number > int_number2:
                max_number2 = int_number
                print("{} больше {}".format(int_number, int_number2))
            elif int_number == int_number2:
                print("{} равно {}".format(int_number, int_number2))
            else:
                max_number2 = int_number2
                print("{} меньше {}".format(int_number, int_number2))

print("Максимальная цифра: {}".format(max_number2))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
print('-----------------------------')
print("Replace vars group operation")
print('-----------------------------')
var1 = input('Input var1: ')
var2 = input('Input var2: ')
print('-- Replace:')
var1, var2 = var2, var1
print("Var1 = {}".format(var1))
print("Var2 = {}".format(var2))


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print("Выражение 'ax² + bx + c = 0'")
a = int(input('Введите значение a'))
b = int(input('Введите значение b'))
c = int(input('Введите значение c'))

discriminant = b ** 2 - 4 * a * c
print('Дискриминант: {}'.format(discriminant))

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Корень 1: {}".format(x1))
    print("Корень 2: {}".format(x2))
elif discriminant == 0:
    x = -b / (2 * a)
    print("Корень: {}".format(x))
else:
    print("Корней нет")