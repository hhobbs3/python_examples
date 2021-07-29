import os

class Greatings:
    def greating(self):
        return "Greatings"

class HelloWorld(Greatings): # extend greatings
    def hello_world(self):
        return "Hello, World"

if __name__ == '__main__':
    h = HelloWorld()
    print(h.hello_world())
    print(h.greating())