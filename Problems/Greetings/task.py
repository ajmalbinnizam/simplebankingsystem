class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am {0}!'.format(self.name))
    # create the method greet here
    
nam = Person(input())
nam.greet()
