''' simple diamond print to console '''


class Diamond():

    side = 0

    def size(self):
        while True:
            side = input("Length of one side? (<return> or 0 to exit): ")
            if not side:
                self.side = side
                break
            if side.isdigit():
                self.side = int(side)
                break
            print('Please enter whole positive number.')

    def __str__(self):
        rows = list(range(self.side))
        output = ""
        for pos in rows + rows[-2::-1]:
            output += f"{'': <{side-pos-1}}{'':*<{pos*2+1}}\n"
        return output


def main():
    print('\nWelcome. Diamond printing awaits...\n')
    while True:
        diamond = Diamond()
        if diamond.size():
            print(diamond)
    print('Bye\n')


if __name__ == "__main__":
    main()
