from sys import argv
script, filename = argv

txt = open(filename)

print("Here's your file,")
print(txt.read())
txt.close()
