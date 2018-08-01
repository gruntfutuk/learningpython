''' trying out decorators again'''

class KnownTags:
    tags = {'p': '/p', 'b': '/b', 'i': '/i', 'class': '/', '-->': '<--'}

def Params(oldFunc):
    def inside(*args, **kwargs):
        print(f'Params: {args}, {kwargs}')
        return oldFunc(*args, **kwargs)
    return inside

def AddTags(*tags):
    def wrapper(wrappedFunc):
        def core(*args, **kwargs):
            line = wrappedFunc(*args, **kwargs)
            for tagblock in reversed(tags):
                tag = tagblock.split('=')[0]
                closetag = KnownTags.tags.get(tag)
                if not closetag: closetag = f'{tag}'
                line = f'<{tag}>{line}<{closetag}>'
            return line
        return core
    return wrapper

@AddTags('-->')
@Params
def Multiply(x, y=10):
    return f'{x} x {y} = {x * y}'

@AddTags('p', 'b', 'x')
def greetings(name):
    return f'Hello {name}, great to meet you. Welcome.'

print(Multiply(3))
print(Multiply(4, 6))
print(Multiply(5, y=7))
print(Multiply(x=4))
print(Multiply(x=7, y=3))

print(greetings('Stuart'))
print(greetings('Lucy'))