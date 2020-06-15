class Father(object):
    def __init__(self):
        print('I,m Father')


class Mother(object):
    def __init__(self):
        print('I,m Mother')


class Human(Father, Mother):

    def __init__(self, name):
        super().__init__()
        self.name = name

        # Because of composition relationship, HumanBody parts are existing here.
        self.head = Head()
        self.body = Body()
        self.legs = [Leg('Right'), Leg('Left')]
        self.hands = [Hand('Right'), Hand('Left')]

        print('I,m Human with all body parts !')


class Head:
    def __init__(self):
        print('Head Existed.')


class Body:
    def __init__(self):
        print('Body Existed.')


class Leg:
    def __init__(self, legSide):
        self.legSide = legSide
        print(f'Leg {self.legSide} Existed.')


class Hand:
    def __init__(self, handSide):
        self.handSide = handSide
        print('Hand {0} Existed.'.format(self.handSide))


if __name__ == '__main__':
    human = Human('Ali')
