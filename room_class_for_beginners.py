''' CLASSES for beginners - simple example '''

class Room():
    def __init__(self, name, height, length, width):
        self.name = name
        self.height = height
        self.length = length
        self.width = width

    @staticmethod
    def mm_to_ft(mm):
        return mm * 0.0032808399

    @staticmethod
    def sqmm_to_sqft(sqmm):
        return sqmm * 1.07639e-5

    def height_in_ft(self):
        return Room.mm_to_ft(self.height)

    def width_in_ft(self):
        return Room.mm_to_ft(self.width)

    def length_in_ft(self):
        return Room.mm_to_ft(self.length)

    def wall_area(self):
        return self.length * 2 * self.height + self.width * 2 * self.height


lounge = Room('Lounge', 1300, 4000, 2000)
snug = Room('Snug', 1300, 2500, 2000)

print(lounge.name, lounge.height, lounge.length, lounge.length)
print(snug.name, snug.height, snug.length, snug.length)

print(lounge.name, 'length in feet:', lounge.height_in_ft())
print(f'{snug.name} wall area: {snug.wall_area()} in sq.mm., ' + \
      f'{snug.sqmm_to_sqft(snug.wall_area()):.2f} in sq.ft.')
 
 
