    from random import choice


    class Game:
        """Based on Game of Lights Off:

        https://dc.ewu.edu/cgi/viewcontent.cgi?article=1166&context=theses

        https://en.wikipedia.org/wiki/Lights_Out_(game)

        """

        LIGHT_ON = "\u25A0"
        LIGHT_OFF = "\u25A1"
        lights = [LIGHT_ON, LIGHT_OFF]
        MAX_COL = 5
        MAX_ROW = 5
        prompt = (
            f"Which light to flip?  (enter alone to exit)\n"
            f"row (0 - {MAX_ROW - 1}), "
            f"col (0 - {MAX_COL - 1}): "
        )

        def __init__(self, kind=None):
            if kind is None:
                self.board_randomizer()
            else:
                self.set_board(kind)
            self.__header = (
                "\nBoard:\n\n   "
                + "".join(f"{col:<2}" for col in range(self.MAX_COL))
                + "\n"
            )
            self.__footer = "\n\n"
            self.play()

        def solved(self):
            return not any([self.LIGHT_ON in row for row in self.board])

        def flip(self, row, col):
            self.board[row][col] = self.lights[self.board[row][col] == self.lights[0]]

        def set_board(self, status):
            self.board = [
                [status for _ in range(self.MAX_COL)] for _ in range(self.MAX_ROW)
            ]

        def board_randomizer(self):
            self.board = [
                [choice(self.lights) for _ in range(self.MAX_COL)]
                for _ in range(self.MAX_ROW)
            ]

        def process_play(self, row, column):
            "flip selected cell and orthogonally ajacent cells"
            self.flip(row, column)
            if row < self.MAX_ROW - 1:
                self.flip(row + 1, column)
            if row > 0:
                self.flip(row - 1, column)
            if column < self.MAX_COL - 1:
                self.flip(row, column + 1)
            if column > 0:
                self.flip(row, column - 1)

        def get_play(self):
            while True:
                response = input(self.prompt)
                if not response:
                    move = ()  # not playing anymore
                    break
                try:
                    row, column = [int(num.strip()) for num in response.split(",")]
                    if 0 <= row <= self.MAX_ROW - 1 and 0 <= column <= self.MAX_COL - 1:
                        move = row, column
                        break
                except ValueError:
                    pass
                print("\nThat is not a valid entry, please try again.\n")

            return move

        def __str__(self):
            body = ""
            for rownum, row in enumerate(self.board):
                body += f'{rownum:>2} {" ".join((row))}' + "\n"
            return self.__header + body + self.__footer

        @staticmethod
        def greeting():
            print(
                """

    Welcome to the Game of Lights Off.

    Given a board with a number of randonmly selected lights
    turned on, your job is to turn all the lights off.

    However, whenever you pick a light to flip from on to off
    or vice versa, lights that are orthoganlly adjacent
    shall also be flipped.

    Mathematically, not all patterns are solveable, but the
    game does not (yet) check that for you.

    You select a light to flip by entering the row and column
    number and both are counted from 0 from the top left.

    Good luck.

            """
            )

        def play(self):  # main game loop for each board
            self.greeting()
            moves = 0
            while not (solved := self.solved()):
                print(self)
                if (move := self.get_play()) :
                    self.process_play(*move)
                    moves += 1
                else:
                    print(f"You finished incompleted after {moves} moves")
                    break
            else:
                print(f"You won with {moves} moves!")


    game = Game()