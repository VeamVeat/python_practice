class DataValidException(Exception):
    pass


def str_to_int(string: str) -> int:
    if string.isdecimal():
        str_number = [f'{i}' for i in range(10)]
        result_list = []
        for id_i, i in enumerate(string):
            for id_j, j in enumerate(str_number):
                if j == i and id_i == len(string) - 1:
                    result_list.append(id_j)
                elif j == i:
                    result_list.append(id_j * 10 ** (len(string) - 1 - id_i))

    else:
        raise DataValidException("Строка " + string + " не является валидной!")
    return sum(result_list)


s_input = input()
print('Введённое число:', s_input, '->', type(s_input))
s = str_to_int(s_input)
print('Преобразованное число:', s, '->', type(s))