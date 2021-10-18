import re


def str_to_int(user_line: str) -> int:
    """
    :param user_line: строка пользователя
    :return: '2345' -> 2000 + 300 + 40 + 5 -> 2345
    """

    num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
    is_number = re.match(num_format, user_line)

    if is_number:

        str_numbers = {'0': 0, '1': 1, '2': 2,
                       '3': 3, '4': 4, '5': 5,
                       '6': 6, '7': 7, '8': 8, '9': 9}

        last_item_in_line = len(user_line) - 1
        result_list = []

        for id_in_user_string, symbol_in_user_string in enumerate(user_line):
            if id_in_user_string == last_item_in_line:
                result_list.append(str_numbers[symbol_in_user_string])
            else:
                result_list.append(str_numbers[symbol_in_user_string] * 10 ** (len(user_line) - 1 - id_in_user_string))

    else:
        raise Exception("Строка " + user_line + " не является валидной!")
    return sum(result_list) if user_line[0] != '-' else sum(result_list) * -1


string_input = input()
print('Введённое число:', string_input, '->', type(string_input))
user_string_input = str_to_int(string_input)
print('Преобразованное число:', user_string_input, '->', type(user_string_input))

