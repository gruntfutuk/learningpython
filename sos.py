# this is file sos.py

import random

class Dog:

    sci_name = "bobo"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "food":
            print("Yummy food!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()


class hiba(Dog):
    origin = "oman"

    def speak(self):
        print("yup")
