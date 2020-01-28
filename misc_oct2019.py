
#%%
while True:
    user_input= input('Please enter number or some text: (return to exit) ').strip()
    if user_input:  # if user entered anything ...
        kind = 'string'  # default, unless discover otherwise
        if user_input.isdigit():  # contains only digits
            kind = 'integer'
        elif user_input.count('.') == 1:  # contains only 1 decimal point
            # extract text before and after decimal point
            before, _, after = user_input.partition('.')
            # and check each of those contains only digits (or nothing after the .)
            if (not before or before.isdigit()) and                 (not after or after.isdigit()) and                 user_input != ".":
                kind = 'float'
        print(f'You entered a {kind}')
    else:
        print('bye')
        break


#%%



#%%



#%%
def is_increasing(arr:list, strict:bool=False) -> bool:
    'return True if list values rise (no duplicates if strict == True)'
    for x, y in zip(arr, arr[1:]):
        if not strict and x > y or strict and x >= y:
            return False
    return True


#%%
is_increasing([4,5,5,6], True)


#%%
def square(num): return num * num
def cube(number): return number * number * number
mynum = int(input('Enter whole number: '))
mynum_squared = square(mynum)
mynum_cubed = cube(mynum)
mynum_power6 = cube(mynum_squared)
print(f'n: {mynum}, ^2: {mynum_squared}, ^3: {mynum_cubed}, ^6: {mynum_power6}')


#%%
mynum_power4


#%%
(2**2)**3


#%%
2**6


#%%
3**6


#%%
with open("scoredetails.txt","w") as file:

    date = input("Enter the date in DDMMYY: ")

    while True:

        membership_no = input("Enter the MembershipNo: (enter to exit) ")
        if not membership_no:
            break

        while True:
            score = input("Enter the score: ")
            if score.isdigit():
                score = int(score)
                if 50 <= score <= 99:
                    break
            print("Wrong score please try again.")

        file.write(f'{date}{membership_no}{score}\n')


#%%
get_ipython().system('cat scoredetails.txt')


#%%
C = [ 7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
print(sum((num for num in C  if num < 0)))


#%%
C = [ 7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

limit = len(C)
idx = 0
total = 0
while idx < limit:
    num = C[idx]
    if num < 0:
        total += num
    idx += 1
print(total)


#%%
def try_me():
    inp = int(input('Please enter an odd number greater than 4: '))
    a = 1
    b=inp-2
    converter = ('*'*inp)

    for j in range(inp):
        print('*'*a)
        a += 2
        if j > inp/2-2:
            break
    print(converter)
    for a in range(inp):
        print('*'*b)
        b -=2


#%%
from io import StringIO


#%%
import sys

class Print_trap(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

        
test_funcs = [diamond]
tests = 3, 5, 11
for test in tests:
    with Print_trap() as target:
        diamond(int(test/2))
    for func in test_funcs:
        with Print_trap() as virt_print:
            func(int(test/2))    
        if virt_print == target:
            print('passed', end='')
        else:
            print('failed', end='')
        newline = f'\n'
        print(f"\n{newline.join(virt_print)}\n")


#%%
with Print_trap() as virt_print:
    try_me()


#%%
virt_print


#%%
try_me()


#%%
def diamond(rows):
    spaces = " " * (rows * 2)
    stars = "* "
    for _ in range(rows):
        print(f"{spaces}{stars}")
        spaces = spaces[2:]
        stars += "* * "
    for _ in range(rows + 1):
        print(f"{spaces}{stars}")
        spaces += "  "
        stars = stars[4:]
        
try:
    height = int(input('Enter height (>4 and odd): '))
    if not height > 4 or not height & 1:
        raise ValueError
except ValueError:
    print('That is not going to work')
    height = None
                  
if height:
    diamond(int(height/2))


#%%
target = '''
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''


#%%
target_list = target.split('\n')[1:-1]


#%%
target_list


#%%
C = [ 7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
x = 0
for c in C: x += c if c < 0 else 0
print(x)


#%%
largest = smallest = None
while True:
    num = input("Enter a number: ").lower().strip()
    if num == "done":
        break
    if num and (num.isdigit() or (num[0] == "-" and num[1:].isdigit())):
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    else:
        print('not a number, please try again')
print(f'Largest is: {largest}, smallest: {smallest}')


#%%
[(0, 'a'), (2, 'b'), (2, 'b'), (7, 'c')] == [(0, 'a'), (2, 'b'), (2, 'b'), (7, 'c')]


#%%
def slice(source, target):
    size_target = len(target)
    size_source = len(source)
    if size_source < size_target:
        raise ValueError('match string longer than source string')
    for idx in range(size_source - size_target):
        yield source[idx:idx+size_target]

target = 'AA'
source = 'abdeeAAbAAAbfde'
counter = 0
for chunk in slice(source, target):
    if chunk == target:
        counter += 1

print(counter)


#%%
with open('delme.txt', 'w') as file:
    text = 'hello world'
    file.write(text)
    
content = open(file.name).read()
print(content)
print(file.closed)


#%%
text


#%%
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1
while counter <= max_index:
    word = words[counter]
    print(word + "!")
    counter = counter + 1


#%%
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(f'{word}!')


#%%
num = 10
while num > 0:
    print(num)
    num = num -1


#%%



#%%
def print_and_dec_to_1(num):
    if num > 0:
        print(num)
        print_and_dec_to_1(num - 1)
    
print_and_dec_to_1(10)


#%%
import hashlib
import time

md5_pass = input("md5>")
md5_file_loc = input("PW List>")

md5_file = open(f'data/{md5_file_loc}', "r")

for counter, password in enumerate(md5_file, start=1):
    hash_obj_1 = hashlib.md5(password.encode('utf-8'))
    hash_obj = hash_obj_1.hexdigest()
    print(hash_obj)

    if hash_obj == md5_pass:
        print(f'\n[Match found]: "{password}"')
        break


#%%
for y, x in enumerate(range(ord("!"), ord("~")+1), start=1):
    print(chr(x), end=('\n' if not y % 10 else ' '))


#%%
print('Great taste')
size = 10
print(f'Count up to {size}')
nums = []
while len(nums) < size:
    try:
        nums.append(int(input('Let: ')))
    except ValueError:
        print('Sorry, not a number, try again.')
print(f'{nums}\n{max(nums)} is Highest Number')


#%%
print('Great taste')
size = 10
print(f'Count up to {size}')
nums = []
while len(nums) < size:
....try:
........nums.append(int(input('Let: ')))
....except ValueError:
........print('Sorry, not a number, try again.')
print(f'{nums}\n{max(nums)} is Highest Number')


#%%
from random import randint

def get_hole_distance():
    while True:
        try:
            hole_distance = int(input("How many meters to the hole (between 195 - 250 inclusive)?"))
            if 195 <= hole_distance <= 250:
                return hole_distance
        except ValueError:
            pass
        print("I'm sorry, you must choose a distance from hole between 195 - 250 inclusive. Please enter again.")

def menu():
    print("\n\nMenu")
    print("(I) Instructions")
    print("(P) Play")
    print("(Q) Quit")
    while True:
        selection = input("Enter your choice").upper()
        if selection and selection in ('I', 'P', 'Q'):
            return selection
        print('Sorry, not an available option. Please try again.')

def instructions():
    print("\n\nThe Golf Game\n\n")


    
    
    
def play(distance, par):
    
    def status():
        print("The game distance is ", game_distance, " as per your request.")
        if shots > par:
            print("After ", shots, " hits, the ball is in the hole! Disappointing. You are ", shots - par,
                  " over par.")
        elif shots == par:
            print("After ", shots, " hits, the ball is in the hole! And that's par.")
        else:
            print("After ", shots, " hits, the ball is in the hole! Congratulations, you are ", par - shots,
                  " under par.")

    def play_a_shot(game_distance, shots, start, fini):
        random_distance = randint(start, fini)
        game_distance = abs((game_distance) - random_distance)
        shots += 1
        result = f"Your shot went {random_distance}m.\n"                  f"You are {game_distance}m from the hole, after {shots} shot/s."
        return result, game_distance, shots    

    shots = 0
    game_distance = distance
    
    while game_distance:
        status()
        print("Enter your choice of club to play with: Enter D for Driver   Enter I for Iron   Enter P for Putter   ")
        select_club = input("Enter your choice").upper()
        if select_club == "D":
            start, fini = 80, 120  
        elif select_club == "I":
            start, fini = 24, 36
        elif select_club == "P":
            if abs(game_distance) < 10:
                start, fini = 1, abs(game_distance)
            else:
                start, fini = 8, 12
        result, game_distance, shots = play_a_shot(game_distance, shots, start, fini)
        print(result)
   
print("Welcome to the Golf Game ")

distance = get_hole_distance()
par = 5
    
while True:
    
    selection = menu()
    
    if selection == "Q":
        print("Thanks for playing")
        break
    
    elif selection == "I":
        instructions()

    else: # must be option P
        play(distance, par)


#%%
print('Great taste')
size = 10
print(f'Count up to {size}')
nums = []
while len(nums) < size:
    try:
        nums.append(int(input('Let: ')))
    except ValueError:
        print('Sorry, not a number, try again.')
print(f'{nums}\n{max(nums)} is Highest Number')


#%%
highest = 0;high = lambda: max(int(input('> ')), highest)
for _ in range(10): highest = high()
print(highest) 


#%%
t = get_higher(0)


#%%
from random import randint

def iffy():
    highest = 0
    for _ in range(1000):
        num = randint(1, 100)
        if num > highest:
            highest = num
    return highest

def maxy():
    return max(set(randint(1, 100) for _ in range(1000)))

get_ipython().run_line_magic('timeit', 'iffy()')
get_ipython().run_line_magic('timeit', 'maxy()')


#%%
from random import choices

def insertion_sort(data:list) -> list:
    'inplace insertion sort'
    for idx in range(1, len(data)):
        current = data[idx]
        while idx > 0 and data[idx - 1] > current:
            data[idx] = data[idx - 1]
            idx -= 1
            data[idx] = current

for _ in range(10):
    data = choices(range(1,100), k=20)
    print(data)
    insertion_sort(data)
    print(data)
    print()


#%%
insertionSort([2,1])


#%%
nums = []
for i in range(0, 10):
    for j in range(i, 10 - i):
        nums.append(i+j)


#%%
while True:
    age = input("Please insert your AGE: ").strip()
    if age and age.isdigit():
        age = int(age)
        if age > 110:
            print('Wow, you must be nearly dead!')
        elif age > 18:
            print("You are Adult")
        elif age < 18:
            print("You are KID")
        elif age == 18:
            print("You are 18")
        break  # escape from while loop
    else:
        print("Please input your fucking AGE")


#%%
def check_for_num(source):
    'checks if source is a string containing valid number (int or float)'
    'returns number of correct type if it is'
    'otherwise returns original object'
    'NB: simple code solution without using try/except'
    
    def is_integer(txt, sign=True):  # so can use for integer and parts of float
        'check string contains only digit, or if sign is True'
        'has an optional + or - sign followed by only digits'
        return txt.isdigit() or (sign and txt[0] in ("-", "+") and txt[1:].isdigit())
    
    if isinstance(source, str):  # check argument is string type
        source = source.strip()  # remove any leading/trailing spaces
        if source:  # check we don't have an empty string
            if is_integer(source):
                source = int(source)
            elif source.count('.') == 1:   # check if there is ONE and only ONE decimal point:
                    before, point, after = source.partition(".")
                    if (not before or is_integer(before) or before in ("+", "-")) and                     (not after or is_integer(after, False)):
                        source = float(source)
        return source
    
    return source  # return original, which could be int, float, or something that's not a string



tests = ['', 'boo', '123', '  -123 ', '4.5', '-0.6', '-.7',
         '  -4.5 ', '+6.', '-.7', 56, -78.9,
         (1, 2), complex(2, 3)
        ]
for test in tests:
    result = check_for_num(test)
    int_or_float = isinstance(result, (int, float))
    print(f'{int_or_float:}\t{test}, {type(result)}')    


#%%
print("What are your numbers?")
total = 0
count = 0
while True:
    x = input('> (enter done to finish) ').strip().lower()
    if x == 'done':
        break
    num = None
    try:
        num = float(x)
        num = int(x)
    except ValueError:
        pass
    if num:
        total += num
        count += 1
        print(f'Count: {count}\tTotal: {total}')
    else:
        print('Invalid entry')

if count > 0:
    print(f'Count: {count}\tTotal: {total}\tAverage: {total/count}') 


#%%
....def bigger_dict(any_dict):  # mutate the passed dictionary
........any_dict['alpha'] = 27.2, 13.8, 8.3
........any_dict['beta'] = ['apple', 'oranges', 'pears']
........any_dict['charlie'] = {78, 46, 92}
........# nothing to return, because we mutated the passed dictionary

....def output_dict(a_dict):  # print contents of dictionary
........for key, value in a_dict.items():
............print(f'key: {key}\t{value}')

....something = {}  # create an empty dictionary
....bigger_dict(something)
....something['zulu'] = {1: 'yuk', 2: 'yak', 3: 'yih'}
....output_dict(something)


#%%
from threading import Thread
class myClass:
    _input = None

    def __init__(self):
        get_input_thread = Thread(target=self.get_input)
        get_input_thread.daemon = True  # Otherwise the thread won't be terminated when the main program terminates.
        get_input_thread.start()
        get_input_thread.join(timeout=20)

        if myClass._input is None:
            print("No input was given within 20 seconds")
        else:
            print("Input given was: {}".format(myClass._input))


    @classmethod
    def get_input(cls):
        cls._input = input("")
        return


#%%
def quick_sort(array):
if len(array) > 1 :
pivot = int( len( array ) -1 )
less = [ ] ; more = [ ]
# Algorithm sequence to be added here.

quick_sort( less ) ; quick_sort( more )

print( '\tLess:' , less , '\tPivot:' , array[ pivot ] , 
'\tMore:' , more )

array[ : ] = less + [ array[ pivot ] ] + more

print( '\t\t...Merged:' , array )

for element in range( len(array ) ) :

value = array[ element ]

if element != pivot :

if value < array[ pivot ] :

less.append( value )

else :

more.append( value )

array = [ 5 , 3 , 1 , 2 , 6 , 4 ]

print( 'Quick Sort...\nArray :' , array )

quick_sort( array )

print( 'Array :' , array )


#%%
def f(a, L=[ ]):
    L.append(a)
    print('L id:', id(L))
    return L

t = f(3)
print(t, id(t))
s = f(1)
print(s, id(s))


#%%
def f(a, L=None):
....if not L:
........L = []
....L.append(a)
....print('L id:', id(L))
....return L

t = f(3)
print(t, id(t))
s = f(1)
print(s, id(s))


#%%
def quick_sort(array):
    if len(array) > 1 :
        pivot = len(array) -1 
        less = [ ] ; more = [ ]
        # Algorithm sequence to be added here.
        quick_sort( less ) ; quick_sort( more )
        print( '\tLess:' , less , '\tPivot:' , array[ pivot ] ,                '\tMore:' , more )
        array[ : ] = less + [ array[ pivot ] ] + more
        print( '\t\t...Merged:' , array )
        for element in range( len(array ) ) :
            value = array[ element ]
            if element != pivot :
                if value < array[ pivot ] :
                    less.append( value )
                else :
                    more.append( value )
array = [ 5 , 3 , 1 , 2 , 6 , 4 ]
print( 'Quick Sort...\nArray :' , array )
quick_sort( array )
print( 'Array :' , array )


#%%



#%%
original = [3, 5, 4, 1, 2, 1, 7, 8, 3, 5]
sub_list = list(set(sorted(original[1:-1])))  # ignore 1st and last, sort rest and remove dups
for check in original[0], original[-1]:  # check to see if 1st or last in what is left
....if check in sub_list:  # found in sub_list so
........sub_list.remove(check)  # remove duplicate item
finished = original[0:1] + sub_list + original[-1:]  # concatenate first, sorted & de-duped, and last
print(finished)


#%%
sub_list


#%%
original


#%%
from random import sample

test = sample(1, 100)
sum_odds = sum_evens = 0
for num in test:
    if num % 2 == 0:
        sum_evens += num
    else:
        sum_odds += num


#%%
lists = [["she", "and","he","and","us","she"],
         [1,2,2,1,1,1,2,1]
        ]

dicts = []

for list_ in lists:
    dict_ = {}
    for item in list_:
        if item in dict_:
            dict_[item] += 1
        else:
            dict_[item]= 1
    dicts.append(dict_)

print(dicts)


#%%
new_dict = {
        'rice': 10,
        'dal': 15,
        'curry': 20,
        'nan': 5,
    }

orderList = ['RicE', 'dAl', 'RICE', 'nan', 'CuRRy', 'dal']
order_items = [item.strip().lower() for item in orderList]
bill = 0
for item in set(order_items):
    bill += new_dict.get(item, 0) * order_items.count(item)
print(bill)


#%%
print('Welcome to the Express lane')
total = 0
for item in 'first', 'second', 'third', 'fourth', 'final':
....price = input(f'Enter the {item:6} price: ')
....try:
........total += float(price)
....except ValueError:
........print('Invalid price, ignored')
sales_tax = total * 0.06
print(f'subtotal:  {total: 6.2f}')
print(f'sales tax: {sales_tax: 6.2f}')
print( '-----------------')
print(f'total:.... {total + sales_tax: 6.2f}')


#%%



