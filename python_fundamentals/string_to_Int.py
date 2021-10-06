import re


def str_to_int(user_string: str) -> int:

    num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
    is_number = re.match(num_format, user_string)

    if is_number:
        str_number = [f'{i}' for i in range(10)]
        result_list = []

        for user_index_in_string, user_symbol_in_string in enumerate(user_string):
            for index_in_str_number, symbol_in_str_number in enumerate(str_number):

                if symbol_in_str_number == user_symbol_in_string and user_index_in_string == len(user_string) - 1:
                    result_list.append(index_in_str_number)

                elif symbol_in_str_number == user_symbol_in_string:
                    result_list.append(index_in_str_number * 10 ** (len(user_string) - 1 - user_index_in_string))

    else:
        raise Exception("Строка " + user_string + " не является валидной!")
    return sum(result_list) if user_string[0] != '-' else sum(result_list) * -1


string_input = input()
print('Введённое число:', string_input, '->', type(string_input))
user_string_input = str_to_int(string_input)
print('Преобразованное число:', user_string_input, '->', type(user_string_input))

