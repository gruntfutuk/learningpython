**Introduction to Classes for Beginners**

A lot of beginners struggle to get their heads around classes, but they are pretty much fundamental to object orientated programming.

I usually describe them as the programming equal of *moulds* used in factories as a template for making lots of things that are identical. Imagine pouring molten iron into a mould to make a simple iron pot.

You might produce a set of instructions to be sold with the pots that tell the owner how to cook using the pot, how to care for it, etc. The same instructions apply to every pot BUT what owners actually do is entirely up to them. Some might make soup, another person a stew, etc.

In Python, a class defines the basics of a possible object and some methods that come with it. (Methods are like functions, but apply to things made using the class.)

When we want create a Python object using a class, we call it 'creating an instance of a class'.

If you have a class called Room, you would create instances like this:

    lounge = Room()
    kitchen = Room()
    hall = Room()

As you typically want to store the main dimensions (height, length, width) of a room, whatever it is used for, it makes sense to define that when the instance is created.

You would therefore have a method called `__init__` that accepts height, length, width and when you create an instance of `Room` you would provide that information:

    lounge = Room(1300, 4000, 2000)

The `__init__` method is called automatically when you create an instance. It is short for initialise (intialize).

You can reference the information using `lounge.height` and so on. These are attributes of the lounge instance.

I provided the measurements in mm but you could include a method (function inside a class) that converts between mm and ft. Thus, I could say something like `lounge.height_in_ft()`.

Methods in classes are usually defined with a first parameter of `self`:

    def __init__(self, height, length, width):

    def height_in_ft(self):

The `self` is a shorthand way of referring to an instance. 

When you use `lounge.height_in_ft()` the method knows that any reference to `self` means the lounge instance, so `self.height` means `lounge.height` but you don't have to write the code for each individual instance. Thus `kitchen.height_in_ft()` and `bathroom.height_in_ft()` use the same method, but you don't have to pass the height of the instance as the method can reference it using `self.height`.

**EXAMPLE Room class**

The code shown as the end of this post will generate the following output:

    Lounge 1300 4000 4000
    Snug 1300 2500 2500
    Lounge length in feet: 4.26509187
    Snug wall area: 11700000 in sq.mm., 125.94 in sq.ft.

Note that a *method definition* that is preceded by the command, `@staticmethod` (a *decorator*) is really just a function that does not include the self reference to the calling instance. It is included in a class definition for convenience and can be called by reference to the class or the instance:

    Room.mm_to_ft(mm)
    lounge.mm_to_ft(mm)

**CLASSES for beginners - simple example**

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
     
Another useful decorator is `@property`, which allows you to refer to a method as if it is an attribute. Not used in the example, but if I put that before the `height_in_ft` methods you could say, for example, `lounge.height_in_ft` instead of `lounge.height_in_ft()`.

One can write classes that are based on other classes. These *child* classes inherit all of the characteristics of the *parent* (or *super*) class but any attribute or method can be *overridden* to use alternatives that apply only to the child (and its children). Such child classes might have additional methods, alternative `__init__` methods, different default output when referenced in a print statement, and so on. The example code code does not demonstrate this feature.