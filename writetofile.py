import os
import sys
import re

filename = 'write.txt'


def fileok(filename):
    while True:

        exists = os.path.exists(filename)
        if not exists:
            print(f"\nThere is no a file with name of {filename}")
        else:
            print(f"\nFile {filename} will be overwrite if you continue.")

        while True:
            user = input(f"\nDo you want to (C)ontinue and use {filename}, (Q)uit, or choose (N)ew file? ").upper()
            if user == "C":
                return filename
            elif user == "Q":
                return False
            elif user == "N":
                break

        while True:
            newname = input('\nEnter new filename: ')
            check = re.match(r'^[\w,\s-]+\.[A-Za-z]{3}$', newname)
            if check:
                if check[0] == newname:
                    filename = newname
                    break
            print('\nSorry, that\'s not a valid filename.')


filename = fileok(filename)
if filename:
    print(f'writing ... to {filename}')
    with open(filename, "w") as file:
        file.write("hey its me i told u it will deleted your previous file")
else:
    print('not writing')