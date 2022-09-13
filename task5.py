# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from sympy import * 

path_1 = 'f1.txt'
path_2 = 'f2.txt'

# Запись многочлена из файла в строку
def read_file(path):
    out_string = ''
    res_txt = open(path, 'r')
    out_string = res_txt.read()
    res_txt.close()

    result_string = out_string[:len(out_string) - 4]
    return result_string  

# Запись многочлена в виде строки в файл
def write_polynomial(input_string: str):
    res_txt = open('task5_res.txt', 'w')
    res_txt.write(input_string)
    res_txt.close()

# Сложение многочленов с помощью символьной логики SymPy
def polynomials_sum(poly_1:str, poly_2:str):
    sum_string = poly_1 + ' + ' + poly_2
    x = Symbol('x')
    sum_string = str(collect(sum_string, x))
    sum_string += ' = 0'
    return sum_string

write_polynomial(polynomials_sum(read_file(path_1), read_file(path_2)))