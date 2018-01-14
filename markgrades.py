# A simple programme to convert marks to grades
#
# Repeatedly prompts user to enter a grade and prints out the marks
# awarded for that grade (or some defined "unclassified" grade/message
# if there is not grade for the mark entered).
#
# On completion, the progamme reports how many valid marks were entered,
# the average mark, and the grade equivelent of that mark (rounded
# down to nearest integer).
#
# A dictionary is used to hold the grade code and the corresponding
# range applicable to each grade. This makes it easy to repurpose
# the code to other kinds of points mapping where there may be
# gaps in the ranges defined.
#
# Optionally, print a frequency table of marks and corresponding grades
#
# If the user enters a non-numeric, a none whole number, or a number outside
# of the range of highest and lowest values defined in the grade table, then
# an error message will be printed and the user will be reprompted.

def main():
    
    def initialise():
        global grades, top, bottom, unclassified, marks, affirmation
        # grade letters and mark ranges defined in dictionary
        # where each grade letter key has a tuple value to hold mark range
        # each tuple should have the highest mark for the grade first
        # * if there are gaps, then unmatched marks will return unclassified
        # * if there are overlaps, any of the matching grades could be returned
        grades = {
                'A': (100, 90),
                'B': ( 89, 75),
                'C': ( 74, 60),
                'D': ( 59, 50),
                'E': ( 49, 40),
                'F': ( 39, 10),
                'X': (  0,  0)
                }
        unclassified = "U (unclassified)"      
        # find highest and lowest allowable marks for entry
        # (not assuming we have a 0 - 100 range)
        top, bottom = highlow(list(grades.values()))
        marks ={}  # keep track of all marks, so we can provide average
        affirmation = ['y', 'yes', 'yeh', 'ok', 'x', '1', 'okay', 'go', 'please', 'yup']
    
    
    def highlow(ranges): # return highest and lower marks possible from grade table
        from operator import itemgetter
        highest = max(ranges, key=itemgetter(1))[0]
        lowest = min(ranges, key=itemgetter(1))[1]
        return highest, lowest
    
    
    def grading(mark, grades):     # find dictionary entry for mark given
        for gradecheck in grades:
            rangecheck = grades[gradecheck]
            if mark in range(rangecheck[1], rangecheck[0]+1):
                return gradecheck
        else: # if mark is not in grade table
            return unclassified
    
    
    def getmark(): # get a valid mark (or just return to exit) from user
        while True:
            markstr = input(f'\nEnter mark: (exit) ')
            if not markstr:  # check for return on own to exit
                return None
            if not markstr.isnumeric():  # check for non numeric input
                print(f'The mark should be a simple whole number.')
                continue
            mark = int(markstr)
            if not bottom <= mark <= top:  # check for out of range input for mark
                print(f'{top} - {bottom} is the allowed range of a mark.')
                continue
            return mark
    
    
    def greeting():
        print('\n\nWelcome to the grading programme\n\n')
        print(f'This programme converts marks in the range {top} to {bottom} to grades:\n')
        print("Grade\t    Marks")
        for grade in grades:
            print(f'{grade:^3s}\t{grades[grade][0]:4d} -{grades[grade][1]:4d}')
        print()
        print('Press enter/return on its own to complete entry of marks.')
    
 
    def averages(marks, grades, out=True):  # print the average mark and corresponding grade
        entries = sum(marks.values())
        total = sum(key * marks[key] for key in marks)
        avmark = total / entries
        avgrade = grading(int(avmark), grades)
        if out:
            print(f'\n\nMarks #{len(marks)}, average: {avmark:.2f} = grade: {avgrade}')
        return avmark, avgrade
    
 
    def table(marks, grades):  # print frequency table of marks if user wants it
        response = input('\nDo you want a table of marks and grades? (Yes) ').rstrip().lower()
        if response in affirmation or not response:
            print('\n\nFrequency table of marks.\n')
            print('Mark Freq    Grade')
            for markfr in sorted(marks.items()):
                print(f'{markfr[0]:4d} {markfr[1]:4d}      {grading(markfr[0], grades)}')
    

    initialise()
    greeting()
    
    # main loop for input of marks and output of grades
    while True:
        mark = getmark()
        if mark is not None:
            marks[mark] = marks.get(mark,0) + 1
            print(f'mark: {mark:4d} = grade: {grading(mark, grades)}')
        else:
            break
    
    # if any valid marks were entered
    if marks:
        averages(marks, grades)  # print average mark and grade
        table(marks, grades)     # optionally print frequence table
    
    print('\n\n== FINISHED ==\n\n')

if __name__ == "__main__":
    grade.main()