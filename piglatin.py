import sys

print ("----------------------------------")
print ("Welcome to the Pig Latin Generator")
print ("----------------------------------")
pyg = 'ay'
if sys.argv[1:]:
    original = sys.argv[1]
else:
    original = ""
print (original, "is the word you entered")
if original and original.isalpha():
    word = original.lower()
    word = word[1:] + word[0] + pyg
    print(f'{word} is the pig latin for {original}')
else:
    print(f"{original} was invalid or you didn't input a name. Please try again")
