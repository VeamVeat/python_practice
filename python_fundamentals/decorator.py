from datetime import datetime
from math import sin, cos


def timeit(func):

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f" Время начала работы функции: {start}\n Время окончания работы функции: {end}\n"
              f" Общее время работы функции: {end - start}\n")
        return result
    return wrapper


@timeit
def calculate_mathematical_expression(number_x: int, number_y: int) -> float:
    return (cos(number_x) * sin(number_y))**sin(number_x + number_y)


result_func = calculate_mathematical_expression(3, 4)
print(result_func)