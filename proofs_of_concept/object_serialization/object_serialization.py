import pickle

class GoesInObject:
    """
      This is a simple object with two private properties accessed by
      public property methods. Its purpose is to be a simple object stored
      in another object as a way to demonstrate the serialization of objects
      which contain other objects in Python.
    """
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

class HoldsObjects:
    """
      This is a simple object with some private properties and a private
      list meant to hold other objects. These properties are accessed by
      public property methods and there is a public method to add objects
      to the object list.
      Its purpose is to be serialized, pickled, and then saved and loaded
      to demonstrate the serialization of objects in Python.
    """
    def __init__(self, name, number):
        self.__object_list = []
        self.__name = name
        self.__number = number
        self.__description = 'I am this object\'s description'
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

    def set_key(self, key, value):
        self.__a_dictionary[key] = value

    def add_object(self, object):
        self.__object_list.append(object)

    # def __str__(self):
    #     return str(vars(self))



def main():
    """
      This function runs he demonstration of serializing objects
      in Python.
    """

    # Create a HoldsObject object and create GoesInObjects with a loop to
    # add to the HoldsObject.
    demo_object = HoldsObjects('Demo Object 1', 1)
    for i in range(5):
        # add_object = GoesInObject(f'Inside Object {i}', i)
        demo_object.add_object(GoesInObject(f'Inside Object {i}', i))
    # Add object to object's dictionary
    key_object = GoesInObject(f'Inside Object 5', 5)
    demo_object.set_key('object-key', key_object)
    # Test print the object
    print(f'Demo object before save: {demo_object}')
    # Pickle and save using with so the file is closed for us.
    with open('demo_save.pkl', 'wb') as file:
        pickle.dump(demo_object, file, protocol=3)
    # Load and unpickle using with so the file is closed for us.
    with open('demo_save.pkl', 'rb') as file:
        load_object = pickle.load(file)
    print(f'Loaded object after save: {load_object}')
    # Check equivalence
    print('Do objects equal each other? ' 
          f'{True if load_object == demo_object else False}')
    # Print properties from original object, and object after loading from
    # save. Loop through lists and print object properties for comparison as
    # well.
    print('\n***** CHECK PROPERTIES *****\n')
    print('Demo object vs Load object--------')
    print(f'Name: {demo_object.name} --- {load_object.name}')
    print(f'Number: {demo_object.number} --- {load_object.number}')
    print(f'Description: {demo_object.description} '
          f'--- {load_object.description}')
    print(f'List items:')
    for i in range(len(demo_object.object_list)):
        print(f'name : number | {demo_object.object_list[i].name} : '
              f'{demo_object.object_list[i].number} '
              f'--- {load_object.object_list[i].name} : '
              f'{load_object.object_list[i].number}')


if __name__ == '__main__':
    main()
