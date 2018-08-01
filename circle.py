import math

class Circle(object):
    """ An advanced circle analytic toolkit - example from Raymond Hettinger
        (see youtube: https://youtu.be/HTLu2DFOdTg)"""


    version = '0.5'         # class variable


    def __init__(self, radius):
        self.radius = radius


    @property
    def radius(self):
        """radius of a circle"""
        return self.diameter / 2.0


    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


    @staticmethod
    def angle_to_grade(angle):
        """Convert angle in degrees to a percentage grade"""
        return math.tan(math.radians(angle)) * 100


    def area(self):
        """Perform quadrature on a shape of a uniform radius"""
        # return math.pi * self.radius ** 2.0
        # alternative area calculation based on perimiter value
        p = self.__perimiter()  # uses private ref in case subclassed and changed
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimiter(self):
        """Calculate perimiter of circle"""
        return math.pi * self.radius * 2

    __perimiter = perimiter # private version in case it is subclassed

    @classmethod
    def frombbd(cls, bbd):
        """Construct a circle from a boundary box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

class Tyre(Circle):
    """Tyres are circles with an adjusted perimiter to account for rubber"""

    def perimiter(self):
        """Circumference adjusted for the rubber"""
        return Circle.perimiter(self) * 1.25

if __name__ == "__main__":

    print(f'Circuitous version: {Circle.version}')
    c = Circle.frombbd(30)
    print(f'A circle of radius {c.radius:.2f}')
    print(f'\thas a perimiter of {c.perimiter():.2f}')
    print(f'\tand an area of {c.area():.2f}')


    t = Tyre.frombbd(30)
    print(f'A tyre of radius {t.radius:.2f}')
    print(f'\thas a perimiter of {t.perimiter():.2f}')
    print(f'\tand an area of {t.area():.2f}')

    print(f'45 degree angle is a {Circle.angle_to_grade(30):.0f}% grade')