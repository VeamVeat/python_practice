import re


def str_to_int(user_string: str) -> int:
    """
    :param user_string: user string
    :return: '2345' -> 2000 + 300 + 40 + 5 -> 2345
    """

    result_int = 0
    start_range = 0
    is_minus = user_string[0] == '-'

    num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
    is_number = re.match(num_format, user_string)

    if not is_number:
        raise Exception("Строка " + user_string + " не является валидной!")
    else:
        if is_minus:
            start_range = 1

        number_dict = {
            '1': 1, '2': 2,
            '3': 3, '4': 4,
            '5': 5, '6': 6,
            '7': 7, '8': 8,
            '9': 9, '0': 0,
        }

        len_user_string = len(user_string)

        for index_user_string in range(start_range, len_user_string - 1):
            number_with_dict = number_dict[user_string[index_user_string]]
            result_int += number_with_dict * (10 ** (len_user_string - 1 - index_user_string))
        result_int += number_dict[user_string[-1]]

        return result_int if not is_minus else result_int * -1


string_input = input()
print('Введённое число:', string_input, '->', type(string_input))
user_string_input = str_to_int(string_input)
print('Преобразованное число:', user_string_input, '->', type(user_string_input))

