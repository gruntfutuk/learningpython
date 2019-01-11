# this is file sos2.py
import sos

class DogPark:

    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("dogs in park:", self, end='\n\n')

    def __repr__(self):
        return ', '.join([dog.name for dog in self.dogs])

    def shout(self, words):
        for dog in self.dogs:
            dog.hear(words)

    def converse(self):
        self.rollcall()
        while True:
            words = input("talk to dogos ('quit' to quit) > ")
            if 'quit' in words.lower():
                print("bye")
                break
            self.shout(words)


if __name__ == '__main__':
    dogs = [sos.hiba("7abebi"), sos.Dog('Rover'), sos.hiba('Poochie')]
    park = DogPark(dogs)
    park.converse()
