
__author__ = 'Манинец Анатолий Андреевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = 345345345

str_number = str(number)
len_number = len(str_number)

print('-----------------------------')
print("Loop 'while'")
print('-----------------------------')
while len_number > 0:
    len_number -= 1
    print(str_number[len_number])

print('-----------------------------')
print("Loop 'while'")
print('-----------------------------')
for symbol in str_number:
    print(symbol)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
print('-----------------------------')
print('Replace vars')
print('-----------------------------')

print('-- Replace vars group operations:')
var1 = input('Input var1: ')
var2 = input('Input var2: ')

print("Var1 = {}".format(var1))
print("Var2 = {}".format(var2))

print('-- Replace:')
var1, var2 = var2, var1

print("Var1 = {}".format(var1))
print("Var2 = {}".format(var2))

print('-- Replace vars intermediate variable:')
var1 = input('Input var1: ')
var2 = input('Input var2: ')

print('Replace:')
var_tmp = var1
var1 = var2
var2 = var_tmp
print("Var1 = {}".format(var1))
print("Var2 = {}".format(var2))

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('-----------------------------')
print('Check age')
print('-----------------------------')
age = input('-- Input age: ')
print("You age: {}".format(age))
if age >= '18':
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')