ml = ['hello', 'world', 'hope', 'you', 'are', 'well']
for word in ml:
    print(word)
words = input('Enter some words: ').strip().split()
for word in words:
    print(f'You said: {word}')
