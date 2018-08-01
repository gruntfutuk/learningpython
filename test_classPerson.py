import unittest
import textwrap
from classPerson import Person
from classPerson import Person_str


class TestPerson(unittest.TestCase):

    def test_peter(self):
        print('Testing ...')
        peter = Person("Peter", "male", job="teacher",
                       phone="1234345", height=1.65)
        peter_text = '''\
                        'name': 'Peter'
                        'sex': 'male'
                        'job': 'teacher'
                        'phone': '1234345'
                        'height': 1.65
                        '''
        peter_text = textwrap.dedent(peter_text)
        self.assertEqual(repr(peter), peter_text)

    def test_mary(self):
        mary = Person("Mary", "female")
        mary_text = '''\
                        'name': 'Mary'
                        'sex': 'female'
                        '''
        mary_text = textwrap.dedent(mary_text)
        self.assertEqual(repr(mary), mary_text)

    def test_john(self):
        john = Person("John", "male", hobby="painting",
                      weight=60, favorite_language="python",
                      nationality="USA")
        john_text = '''\
                        'name': 'John'
                        'sex': 'male'
                        'hobby': 'painting'
                        'weight': 60
                        'favorite_language': 'python'
                        'nationality': 'USA'
                        '''
        john_text = textwrap.dedent(john_text)
        self.assertEqual(repr(john), john_text)

    def test_wendy(self):
        print('Testing ...')
        peter = Person_str("Wendy", "female", job="teacher",
                           phone="1234345", height='1.35')
        peter_text = '''\
                        'name': 'Wendy'
                        'sex': 'female'
                        'job': 'teacher'
                        'phone': '1234345'
                        'height': '1.35'
                        '''
        peter_text = textwrap.dedent(peter_text)
        self.assertEqual(repr(peter), peter_text)

    def test_barry(self):
        mary = Person_str("Barry", "male")
        mary_text = '''\
                        'name': 'Barry'
                        'sex': 'male'
                        '''
        mary_text = textwrap.dedent(mary_text)
        self.assertEqual(repr(mary), mary_text)

    def test_helen(self):
        john = Person_str("Helen", "female", hobby="painting",
                          weight='40', favorite_language="python",
                          nationality="USA")
        john_text = '''\
                        'name': 'Helen'
                        'sex': 'female'
                        'hobby': 'painting'
                        'weight': '40'
                        'favorite_language': 'python'
                        'nationality': 'USA'
                        '''
        john_text = textwrap.dedent(john_text)
        self.assertEqual(repr(john), john_text)


if __name__ == "__main__":
    unittest.main()
