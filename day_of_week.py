''' determine day of week for any Gregorian date '''

# based on formulae at https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html

DOW = dict(enumerate(('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')))
MONTHS = dict(enumerate(('January', 'February', 'March', 'April',
                       'May', 'June', 'July', 'August',
                       'September', 'October', 'November', 'December'), start=1))



def is_leap_year(year):
    'return True/False if year is a leap year'
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_date(msg):
    'get date from user and return tuple of dd, mm, yyyy'
    while True:
        response = input(msg).strip().split('/')
        if response and len(response) == 3:
            try:
                dd, mm, yyyy = [int(x) for x in response]
                if not 1 <= dd <= 31:
                    raise IndexError('Day must be between 1 and 31')
                if not 1 <= mm <= 12:
                    raise IndexError('Month must be between 1 and 12')
                if not 1582 <= yyyy <= 9999:
                    raise IndexError('Year must be between 1582 and 9999')
                if mm == 2 and dd > 28:
                    if not is_leap_year(yyyy) or dd > 29:
                        raise IndexError(f'Too many days for {MONTHS[2]} in {yyyy}')
                if dd == 31 and mm not in (1, 3, 5, 7, 8, 10, 12):
                    raise IndexError(f'Too many days for {MONTHS[mm]}')
                return dd, mm, yyyy
            except ValueError as e:
                print(f'{response} can not be understood as a date such as 18/05/1958')
            except IndexError as e:
                print(e)
        else:
            print('A response in the required format is expected. Please try again.')

def day_of_week(dd, mm, yyyy):
    'return day of week for date dd/mm/yyyy'
    mm = mm - 2  # march = 1, jan = 11
    if mm < 1:
        mm + 12
    if mm >= 11:  # year - 1 if month is jan or feb
        yyyy -= 1

    C = int(yyyy / 100)
    Y = yyyy % (C * 100)
    W = (dd + int(2.6 * mm - 0.2) - 2 * C + Y + int(Y/4) + int(C/4)) % 7

    return DOW[W]

dd, mm, yyyy = get_date('Please enter date of birth in form: dd/mm/yyyy: ')
print(f'{dd}/{mm}/{yyyy} is a {day_of_week(dd, mm, yyyy)}')
