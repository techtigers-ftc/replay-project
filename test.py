class Animal:
    def __init__(self):
        self._food_level = 10

    def speak(self):
        print('!! not implemented !!')

    def eat(self, amount):
        self._food_level += amount

    def run(self, time):
        self._food_level -= (time * 2)

    def show(self):
        print('Food level: {}'.format(self._food_level))



class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print('woof woof')


d = Dog()
d.eat(10)
d.run(1)
d.speak()
d.show()

print(d isinstance(Animal))

class DisplayAdapter:
    def __init__(self):
        pass

    def initialize(self):
        pass

    def show(self, display):
        if display is None:
            raise ValueError("Cannot render ui - display is not provided")


class AsciiDisplayAdapter(DisplayAdapter):
    def __init__(self):
        super().__init()
        pass


    def show(self, display):
        super.show(display)
        # Now do the actual display logic for the ascii display

