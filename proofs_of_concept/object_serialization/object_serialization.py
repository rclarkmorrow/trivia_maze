class HoldsObjects:
    def __init__(self, name, number, object):
        self.__object_list = [object]
        self.__name = name
        self.__number = number
        self.__description = 'I am this objects description'
        self.__a_dictionary = {
            'a_key': 'I am some value for a key',
            'b_key': 3,
            'c_key' : {
                'nested_key': 'I am a nested key'
            },
            'object_key': ''
        }

    @property
    def object_list(self):
        return self.__object_list

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def description(self):
        return self.__description

    @property
    def a_dictionary(self):
        return self.__a_dictionary

    def add_object(self, object):
        self.__object_list.append(object)

    def __str__(self):
        return str(vars(self))



def main():
    print('hello world!')

if __name__ == '__main__':
    main()