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
# On completion, mark and grade averages and grades are ouput
#
# If the user enters a non-numeric, a none whole number, or a number outside
# of the range of highest and lowest values defined in the grade table, then
# an error message will be printed and the user will be reprompted.
#
# A mark of 0 is assumed to be an excluded mark (not included in frequency table
# unless it is explicitly included in the grade table)


if __name__ == "__main__":
    from collections import namedtuple
    from collections import defaultdict
    import re

    # grade letters and mark ranges defined in dictionary
    # where each grade letter key has a tuple value to hold mark range
    # each tuple should have the highest mark for the grade first
    # * if there are gaps, then unmatched marks will return unclassified
    # * if there are overlaps, any of the matching grades could be returned

    MarkRange = namedtuple('MarkRange', 'top bottom description')
    GradeResult = namedtuple('GradeResult', 'grade description')
    grades = {
        'A': MarkRange(top=100, bottom=90, description='Distinction'),
        'B': MarkRange(top=89, bottom=75, description='Merit'),
        'C': MarkRange(top=74, bottom=60, description='Good Pass'),
        'D': MarkRange(top=59, bottom=50, description='Pass'),
        'E': MarkRange(top=49, bottom=40, description='Poor'),
        'U': MarkRange(top=39, bottom=10, description='** FAIL **')
    }

    excluded = GradeResult("X", "excluded")
    marksfreq = defaultdict(int)  # keep track of all marks, so we can provide average
    endentry = frozenset(['', 'q', 'x', 'end', 'exit', 'quit', 'bye', 'fini', 'finished'])

    def highlow(markrange):  # return highest and lower marks possible in a MarksRange tuple list
        from operator import attrgetter
        highest = max(markrange, key=attrgetter('top'))
        lowest = min(markrange, key=attrgetter('bottom'))
        return highest.top, lowest.bottom

    possiblemarks = list(grades.values())
    top, bottom = highlow(possiblemarks)
    print(f'top = {top}, bottom = {bottom}')

    def grading(mark, grades):  # find dictionary entry for mark given
        for gradecheck, marks in grades.items():
            if mark in range(marks.bottom, marks.top + 1):
                return GradeResult(gradecheck, marks.description)
        else:  # if mark is not in grade table
            return excluded

    def invalidmarkmsg(markstr, zeroexclude=False):
        print(f'{markstr} is not a valid entry.')
        print(f'Allowed range is: {top} - {bottom}', end='')
        if zeroexclude: print(f', or 0 for grade {excluded.grade} ({excluded.description})', end='')
        print('.')

    def getmarks(marks, grades):  # get a valid mark (or just return to exit) from user
        while True:
            markstr = input('\nEnter mark: (exit) ')
            if markstr.lower() in endentry: return False

            markstrs = [mrk for mrk in re.split(' |,|;|, |; ', markstr) if mrk != '']

            for markstr in markstrs:
                if not markstr.isnumeric():  # check for non numeric input
                    invalidmarkmsg(markstr, zeroexclude=bottom > 0)
                    continue

                mark = int(markstr)
                if (mark == 0) or (bottom <= mark <= top):
                    grade = grading(mark, grades)
                    print(f'mark: {mark:4d},  grade {grade.grade} ({grade.description})')
                    if bottom <= mark <= top:
                        marks[mark] += 1
                else:
                    invalidmarkmsg(markstr, zeroexclude=bottom > 0)

    def greeting(grades):
        print('\n\nWelcome to the grading programme\n\n')
        print(f'This programme converts marks in the range {top} to {bottom} to grades:\n')
        print("Grade\t    Marks")
        for grade, markrange in grades.items():
            print(f'{grade:^3s} {markrange.description:13s} {markrange.top:4d} -{markrange.bottom:4d}')
        print('\nOn completion of entry of marks, an average mark and grade equivalence will be output')
        print('followed by a marks by grade frequency table.\n')
        print('\nPress enter/return on its own to complete entry of marks.')
        print('(Multiple grades may be entered on one line, using commas for seperation.)')

    def outputaverages(marksfreq, grades, out=True):  # print the average mark and corresponding grade
        if len(marksfreq) == 0: return
        entries = sum(marksfreq.values())
        total = sum(mark * freq for mark, freq in marksfreq.items())
        avmark = total / entries
        avgrade = grading(int(avmark), grades)
        if out:
            print(f'\n\nMarks #{len(marksfreq)}, average: {avmark:.2f}, grade {avgrade.grade} ({avgrade.description})')
        return avmark, avgrade

    def outputfreqtables(marksfreq, grades):
        if len(marksfreq) == 0: return

        print('\n\nFrequency table of marks.\n')
        print('Mark  Freq  Grade')
        gradesfreq = defaultdict(int)

        for markfr in sorted(marksfreq.items(), reverse=True):
            graded = grading(markfr[0], grades)
            gradesfreq[graded.grade] += markfr[1]
            print(f'{markfr[0]:4d}  {markfr[1]:4d}  {graded.grade} ({graded.description})')

        print('\n\nFrequency table of grades.\n')
        print('Grade  Freq  Description')

        for gradefr in sorted(gradesfreq.items()):
            print(f'{gradefr[0]:4s}  {gradefr[1]:4d}  {grades[gradefr[0]].description}')

    ###################################
    #   main routine
    ###################################

    greeting(grades)
    getmarks(marksfreq, grades)
    outputaverages(marksfreq, grades)
    outputfreqtables(marksfreq, grades)
    print('\n\n== FINISHED ==\n\n')
