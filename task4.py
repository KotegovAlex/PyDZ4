# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
    # Пример:
    # k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint


k = int(input("Задайте натуральную степень k -> "))

def create_polynomial(input_degree: int):
    res_string = ''
    temp = []
    coeff_list = []

    for i in range(0, input_degree + 1):
        # создается список коэффициентов
        coeff_list.append(randint(0, 100)) 
        # формирование многочлена в виде списка
        values = (i, coeff_list[i]) 
        match values:
            case (0, 0) | (1, 0) | (_, 0):
                continue
            case (0, _):
                temp.append(f'{coeff_list[i]}')
            case (0, 1):
                temp.append(f'x')
            case (_, 1):
                temp.append(f'x**{i}')
            case (1, _):
                temp.append(f'{coeff_list[i]}*x')
            case (_, _):
                temp.append(f'{coeff_list[i]}*x**{i}')
    temp.reverse()
    res_string = ' + '.join(temp)
    res_string += ' = 0'
    print(coeff_list)
    return res_string

def write_polynomial(input_string: str):
    input = open('text.txt', 'w')
    input.write(input_string)
    input.close()

write_polynomial(create_polynomial(k))