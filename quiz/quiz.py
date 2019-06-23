from question.question import Question

question_prompts = [
    '''Who was the person that founded intel:
    \n(A) Robert Moore \n(B) Gordon Moore \n(C) Robert Noyce \n(D) Gordon Noyce\n\n''',
    '''Which one of these is disgusting:
    \n(A) Burger King foot fungus \n(B) Pineapple on pizza \n(C) diarrhea \n(D) All of the
above!\n\n'''
]

questions = [
    Question(question_prompts[0], "B" or "C"),
    Question(question_prompts[1], "B"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
