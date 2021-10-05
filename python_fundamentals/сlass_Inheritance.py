class First:
    def get_name(self):
        return f'{self.__class__.__name__}'

    @staticmethod
    def get_type():
        return 'Class'


class Second(First):
    @classmethod
    def get_name(cls):
        return f'{cls.__class__.__name__}'


class Third:
    def get_programming_language(self):
        return "Python"


class GeneralOne(Second, Third, First):
    pass


class GeneralTwo(Second, Third, First):
    def get_programming_language(self):
        super().get_programming_language()
        return "Python-love"


class GeneralThree(Second, Third, First):
    pass


a = GeneralOne()
print(a.get_name())

b = GeneralTwo()
print(b.get_programming_language())

c = GeneralThree()
print(c.get_type())
print(GeneralThree.get_type())


