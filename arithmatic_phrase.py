from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
import operator
from random import randint

program = "Firstly add the numbers then divide and multiple and lastly subtract"
tokens = word_tokenize(program)
stop_words = set(stopwords.words('english'))
remove_tokens = ["I", "want", "make", "program", "lastly"]
clean_tokens = [token for token in tokens
                if token not in stop_words
                and token not in remove_tokens]

variables = [(float(randint(0, 30)), float(randint(0,30))) for _ in range(randint(5, 15))]
operations = {'add': operator.add,
              'subtract': operator.sub,
              'multiple': operator.mul,
              'divide': operator.truediv
                }

for a, b in variables:
    for token in clean_tokens:
        if token in operations:
            try:
                answer = operations[token](a, b)
            except Exception as inst:
                print(f'** ERROR ** {inst} for {a} {token} {b}')
            else:
                print(f'{a:2.0f} {token:^9} {b:2.0f} = {answer:6.2f}')
        else:
            print(f'{a:2.0f} {token:^9} {b:2.0f} = no such operation')