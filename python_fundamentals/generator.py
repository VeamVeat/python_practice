
def my_generator(list_of_string: list) -> int:
    for line_in_the_list in list_of_string[::-1]:
        yield len(line_in_the_list)


my_list = ['one', 'two', 'three', 'long_number']
item_in_my_list = my_generator(my_list)


for item in my_list:
    print(next(item_in_my_list))
