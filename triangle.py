''' Beginner Python exercise to print an Isosceles triangle of asterisks with a user specified number of asterisks
	in the base (reduced by one to odd number if an even number is supplied). There is a space between each asterisk.
'''

''' one liner - cryptic '''
def triangle_in_one():
    print(*(" " * i + " *" * j for j, i in enumerate(range(int((int(input('Base size: ')) + 1) / 2) * 2, 0, -1))), sep="\n")

def triangle(base: int) -> str:
    ''' return print string of asterisk triangle of indicated base size '''
    if not isinstance(base, int):
        raise TypeError(f'{base} not valid - triangle function requires an integer parameter')
    if base < 2:
        raise ValueError(f'{base} not valid - triangle function requires a positive integer over 1 parameter')
    apex = int((base + 1) / 2) * 2
    triangle_str = ''
    for asterisks, spaces in enumerate(range(apex, 0, -1)):
        triangle_str += (f'{" " * spaces}{" *" * asterisks}\n')
    return triangle_str

if __name__ == "__main__":
    triangle_in_one()
    print(triangle(int(input('Base size: '))))