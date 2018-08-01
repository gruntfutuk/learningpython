''' example of class with a few fixed arguments and arbirary
    number of additional keyword/attribute arguments '''


class Person:

    def __init__(self, name, gender='n/a', **kwargs):
        self.name = name
        self.sex = gender
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __repr__(self):
        return '\n'.join([f'{repr(k)}: {repr(v)}' for k, v in vars(self).items()]) + "\n"


class Person_str(Person):

    @staticmethod
    def checkstr(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(
                    f'Only string attributes are allowed. {arg} is not a string value.')
        return True

    def __init__(self, name, gender='n/a', **kwargs):
        if self.checkstr(name, gender, *kwargs.values()):
            super().__init__(name, gender, **kwargs)


def main():
    ''' example usage of Person class, any number of attributes can be specified '''

    # with non-string parameters
    peter = Person("Peter", "male", job="teacher",
                   phone="1234345", height=1.65)
    mary = Person("Mary", "female")
    john = Person("John", "male", hobby="painting",
                  weight=60, favorite_language="python",
                  nationality="USA")

    print(peter)
    print(mary)
    print(john)

    # with string only parameters allowed
    wendy = Person_str("Wendy", "female", job="teacher",
                       phone="1234345", height='1.35')
    barry = Person_str("Barry", "male")
    helen = Person_str("Helen", "female", hobby="painting",
                       weight='40', favorite_language="python",
                       nationality="USA")

    print(wendy)
    print(barry)
    print(helen)


if __name__ == "__main__":
    main()
