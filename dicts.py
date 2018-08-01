from __future__ import division, print_function
import sys

class UserProperty:
    def __init__(self, v0, v1, v2, v3, v4):
        self.guido = v1
        self.sarah = v1
        self.barry = v2
        self.rachel = v3
        self.tim = v4

    def __repr__(self):
        return 'UserProperty(%r %r %r %r %r)' \
            % (self.guido, self.sarah, self.barry, self.rachel, self.tim)

colors = UserProperty('red', 'green', 'blue', 'indigo', 'pink')
cities = UserProperty('London', 'Manchester', "Derby", 'Telford', 'Stafford')
fruits = UserProperty('apple', 'orange', 'peach', 'pear', 'grapefruit')

for user in [colors, cities, fruits]:
    print(vars(user))

print(list(map(sys.getsizeof, map(vars, [colors, cities, fruits]))))