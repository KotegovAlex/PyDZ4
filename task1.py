# 1. Вычислить число π c заданной точностью d
    # Пример:
    # при $d = 0.001, π = 3.141

from math import *

d = input('Введите желаемую точность d (например, 0.01) -> ')

def user_accuracy(accuracy: str):
    temp = str(pi)
    return temp[:len(accuracy)]
    
print(user_accuracy(d))