# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
    # [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

seq_1 = [1, 1, 2, 3, 4, 5, 5]

def non_repeating_list(input_sequence:list):
    res = []
    
    input_sequence.sort()
    for i in input_sequence:
        if input_sequence.count(i) > 1: # count считает количество совпадений i в исходном списке
            continue
        else:
            res.append(i)
    return res

print(non_repeating_list(seq_1))