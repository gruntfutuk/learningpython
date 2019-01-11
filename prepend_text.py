'adds some text to the beginning of a file, and moves the'
'rest of the content down the file'

new_text = 'This is new text with a 😮 to make you laugh'
buffer = new_text.encode('utf-8')
size = len(buffer)

with open('buffer.txt', 'r+b') as f:
    while buffer:
        next_buffer = f.read(size)
        f.seek(-len(next_buffer), 1)
        f.write(buffer)
        buffer = next_buffer
