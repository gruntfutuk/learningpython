from random import randint

num1 = randint(1,10)
num2 = randint(1,10)
answer = num1 * num2
q1 = int(input(f'Question 1: {num1} X {num2} = '))
if q1 == answer:
    print('Correct')
else:
    print(f'Incorrect, the answer is {answer}')