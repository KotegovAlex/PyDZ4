# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
    # "20" -> [2, 2, 5]

from queue import Empty
import sympy as s # после pip install sympy

number = int(input('Введите натуральное число N -> '))

def simple_mults(number: int):
    res = []
    temp = number
    for i in s.primerange(2, number):
        while temp % i == 0:
            res.append(i)
            temp /= i
    if len(res) < 1:
        return f"{number} - это простое число"
    else:
        return res

print(simple_mults(number))