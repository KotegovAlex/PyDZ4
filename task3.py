# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
    # [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

seq_1 = [1, 1, 2, 3, 4, 5, 5]

def non_repeating_list(input_sequence:list):
    res = []
   
    for i in range(1, len(input_sequence) - 1):
        if (input_sequence[i] == input_sequence[i - 1]) or (input_sequence[i] == input_sequence[i + 1]):
            continue
        else:
            res.append(input_sequence[i])
    return res

print(non_repeating_list(seq_1))