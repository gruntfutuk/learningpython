#!/usr/bin/python
# typical usage of generator & iterator

# method 1
def foo(item_list):
    for item in item_list:
        yield item

items = ['a','b','c']
iter = foo(items)
for item in iter:
    print item

# method 2, less common but showing how to use next()
print '\n'    # newline
iter = foo(items)
while True:
    try:
        print iter.next()
    except StopIteration:
        print "done"
        break

# method 3
print '\n'
content = "hello world > this is the future > python"
split_iter = iter(content.split('>'))
print split_iter
for next_item in split_iter:
    print next_item.strip()  # remove unnecessary white space[B
