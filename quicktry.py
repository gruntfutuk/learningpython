print('Creating a text file with the write() method.')
text_file = open('write_it.txt', 'w+')

text_file.write('Line 1\n')
text_file.write('This is line 2\n')
text_file.write('That makes this line 3\n')

text_file.seek(0)
print(text_file.read())
text_file.close()

print('\nCreating a text file with the writelines() method.')
text_file = open('write_it.txt', 'w+')
lines = ['Line 1\n',
         'This is line 2\n',
         'That makes this line 3\n']
text_file.writelines(lines)
text_file.seek(0)
print(text_file.read())
text_file.close()

print('\nReading the newly created file.')
text_file = open('write_it.txt', 'r')
print(text_file.read())
text_file.close()

while True:
    print("I'm tapping my fingures.")
    name=input('Name (or enter to end):')
    if not name:
        break
    print(f'Hello {name}. Good to meet you.')
