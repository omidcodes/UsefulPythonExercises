from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('I am a DOG! my name is :{}'.format(self.name))


class Cat(Animal):
    def talk(self):
        print('I am a CAT! my name is :{}'.format(self.name))


if __name__ == '__main__':
    #a = Animal('Rex')      # Raises an Error. because Animal is an abstract class.

    mydog = Dog('Jessie')
    mydog.talk()

    mycat = Cat('Kitty')
    mycat.talk()
