class Person:

    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    @property
    def id(self):
        return f'#{self.__id}#'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property           #name.getter
    def name(self):     #get_name
        return f'*{self.__name}*'
    
    @name.setter       
    def name(self, new_name): #def set_name(self, new_name):
        if len(new_name) < 4:
            print ('Too short!!')
            return
        self.__name = new_name
    
    def __repr__(self):
        return f'Person: ({self.__id}, {self.__name}, {self.__age}'

    def __str__(self):
        return f'Person: ID: {self.__id}, Name: {self.__name}, Age: {self.__age}'