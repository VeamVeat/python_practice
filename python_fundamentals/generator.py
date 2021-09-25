
def my_generator(list_of_string: list) -> int:
    string_length = len(list_of_string)
    for line_in_the_list in range(string_length):
        yield len(list_of_string[string_length - line_in_the_list - 1])


my_list = ['one', 'two', 'three', 'long_number']
item_in_my_list = my_generator(my_list)


for item in range(len(my_list)):
    print(next(item_in_my_list))
