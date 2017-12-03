# how to use generators/iterators ** the basics **
 
# basic generator
def foo(item_list):
    for item in item_list:
        yield item

# consuming
items = ['x','y','z']
iter = foo(items)
for item in iter:
    print(item)
 
# consuming using next - with trap for when no more entries
iter = foo(items)
while True:
    try:
        print(iter.next())
    except StopIteration:
        print('All done')
        break
 
# generators and strings
phrase = 'Mary had a little lamb>White fleece>Four legs'
line_iter = iter(phrase.split('>'))
print(line_iter)
for next_line in split_iter:
    print(next_line)