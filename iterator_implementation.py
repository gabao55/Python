class MyList:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    def __getitem__(self, index):
        if index >= len(self.__items):
            raise IndexError('List index out of range')

        return self.__items[index]

    def __setitem__(self, key, value):
        if key >= len(self.__items):
            self.__items.append(value)

        self.__items[key] = value

    def __delitem__(self, key):
        del self.__items[key]

    def __iter__(self):
        return self

    def __next__(self):

        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item

        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

if __name__ == '__main__':
    lista = MyList()
    lista.add('Roger')
    lista.add('Peter')

    print(lista)

    for value in lista:
        print(value)

    print(lista[1])

    lista[2] = 'Jhon'

    print(lista[2])

    del lista[2]

    print(lista)