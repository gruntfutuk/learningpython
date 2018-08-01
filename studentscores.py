''' collect set of student marks '''

import csv


def greeting():
    print('\n\n')
    print('Welcome to the student marks recording system.\n')
    print('You should enter marks in the following format:')
    print('student name, subject1 score1 score2 score3, subject2 score1 score2 score3')
    print()
    print('Thus, for subjects with more than one score, use a space to seperate scores from each other')
    print('Score(s) will be given a subject name of unassigned-001, etc, if subject name is missing')
    print()


def list_students(student_marks):
    print('\n\nStudent Marks')
    for name, marks in student_marks.items():
        print(f"Name: {name}:- ")
        averages = []
        for markname, marks in marks.items():
            total = sum([int(mark) for mark in marks])
            average = 0 if total == 0 else total / len(marks)
            averages.append(average)
            print(f'\t{markname:10s}: {", ".join(marks):20s} (av: {average:.2f})')
        total = sum(averages)
        average = 0 if total == 0 else total / len(averages)
        print(f'\n\tOverall average mark:\t\t {average:.2f}')
        print()
    print()


def get_student_marks():

    student_marks = {}

    while True:
        line = input('Name and marks? (return to end) ')
        if line:
            elements = list(*csv.reader([line]))
            name = elements[0]
            marks = {}
            unassigned = 1
            for score_line in elements[1:]:
                scores = score_line.strip().split()
                if scores[0].isdigit():
                    markname = f"unassigned-{unassigned:03d}"
                    unassigned += 1
                else:
                    markname = scores.pop(0)
                marks[markname] = list(scores)
            student_marks[name] = marks
        else:
            return student_marks


def main():
    greeting()
    student_marks = get_student_marks()
    list_students(student_marks)


if __name__ == "__main__":
    main()
