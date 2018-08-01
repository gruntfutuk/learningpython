# outputs details of employee(s) with highest salary
import ipdb

def main():


    def printhighest(highest):  # same printout for highest and equalhigh rows
        print(f'Name: {highest[0]}, Pay: {highest[1]}')
        print(f'University/Office: {highest[2]}, position: {highest[3]}\n')


    import csv

    my_file = open('IndianaSALARIES.csv', 'r')

    list_of_lines = csv.reader(my_file, delimiter=',')
    next(list_of_lines, None) # skip header row

    highestpay = 0  # highest pay found in csv file
    highest = []    # copy of row with highest pay
    equalhigh = []  # copies of all rows that match highest pay found
    ipdb.set_trace()
    for line_items in list_of_lines:

        # pay is in second position, ignore leading $ and any commas
        pay = int(line_items[1][1:].replace(',',''))

        if pay > highestpay:
            highestpay = pay        # note highest pay so far
            highest = line_items    # copy of highest pay row so far
            equalhigh = []          # new high, so reset equalhigh entries
        elif pay == highestpay:     # new record matches current highest
            equalhigh.append(line_items)  # so keep note of this row

    if highest:  # if we found any records with salary > 0
        print('Highest paid:\n')
        printhighest(highest)

    if equalhigh:  # if there were any equally high pay records
        for highest in equalhigh:
            printhighest(highest)

if __name__ == "__main__":
    main()
