from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk


def writeprogramme(operation):
    with open("programme.py", "a") as op:
        op.write(operation + "\n")


program = "I want to make a program which can divide, add, divide and subtract"
tokens = word_tokenize(program)
stop_words = set(stopwords.words('english'))
remove_tokens = ["I", "want", "make", "program", ","]
clean_tokens = [token for token in tokens
                if token not in stop_words
                and token not in remove_tokens]

print(f'Tokens to process: {", ".join(clean_tokens)}')

variables = {'a': 'a = 64', 'b': 'b = 10.0'}
operations = {'add': 'print(a + b)',
              'subtract': 'print(a - b)',
              'multiple': 'print(a * b)',
              'divide': 'print(a / b)'}

for variable in variables.values():
    print(f'Variable: {variable}')
    writeprogramme(variable)

for token in clean_tokens:
    print(f'print(operation): {operations[token]}')
    writeprogramme(operations[token])
