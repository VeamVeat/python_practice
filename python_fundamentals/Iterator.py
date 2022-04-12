
class MyIterator:
    def __init__(self, initial_number):
        self.number_to_square = initial_number
        self.start = 0

    def __next__(self):
        if self.start == len(self.number_to_square):
            raise StopIteration
        else:
            next_element = self.number_to_square[self.start]
            self.start += 1
            return next_element

    def __iter__(self):
        return self


string = 'wis'
iterator = MyIterator(string)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
