from math import sin, cos
from datetime import datetime


class Timer:

    def __init__(self, fun):
        self.function = fun

    def __call__(self, *args, **kwargs):
        start_time = datetime.now()
        result = self.function(*args, **kwargs)
        end_time = datetime.now()
        print(f" Время начала работы функции: {start_time}\n Время окончания работы функции: {end_time}\n"
              f" Общее время работы функции: {end_time - start_time}\n")
        return result


@Timer
def calculate_mathematical_expression(number_x: int, number_y: int) -> float:
    return (cos(number_x) * sin(number_y))**sin(number_x + number_y)


result_func = calculate_mathematical_expression(3, 4)
print(' Результат функции: ', result_func)
