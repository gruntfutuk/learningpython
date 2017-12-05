import re
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('word', help="specify word to search for in a file")
    parser.add_argument('fname', help="specify name of file to search")
    args = parser.parse_args()

    searchFile = open(args.fname)
    lineNum = 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word, line, re.M | re.I)
        if searchResult:
            print(f'{lineNum:5d} : {line}')

if __name__ == "__main__":
    main()
