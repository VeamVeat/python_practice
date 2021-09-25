

class MyIterator:
    def __init__(self, initial_number):
        self.number_to_square = initial_number
        self.index = 0

    def __next__(self):
        if self.index <= len(self.number_to_square) - 1:
            i = self.index
            self.index += 1
            return self.number_to_square[i]
        else:
            raise StopIteration

    def __iter__(self):
        return self


string = 'wis'
iterator = MyIterator(string)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))