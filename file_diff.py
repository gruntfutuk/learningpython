    def check_files(*file_handles):
        '''line by line comparison of multiple text files, returns on first detection of
        a difference between any of the files and returns the number of the line it was found
        on and a copy of the line from each file in a list

        also detects if any of the files are longer, returns the number of the line where one or
        more files stop, and a copy of the next line of all longer files

        if files are identical, returns None and None for the line count and list of lines

        arguments are the file handles'''

        def next_line(file_handle):
            '''return next line of file or None if no more lines'''
            try:
                line = next(file_handle)
            except StopIteration:  # reached end of file
                return None
            else:
                return line

        count = 1  # file(s) line number
        while True:
            lines = []  # to store copy of next line of each file
            for file_handle in file_handles:
                lines.append(next_line(file_handle))
            if set(lines) == {None}:  # reached end of all files
                return None, None
            if None in lines:  # reached end of one or more but not all files
                return -count, lines
            if len(set(lines)) > 1:  # line differences found
                return count, lines
            count += 1


if __name__ == '__main__':

    import contextlib

    # need to make sure these files exist
    filenames = 'd1.txt', 'd2.txt', 'd3.txt', 'd4.txt'

    with contextlib.ExitStack() as stack:
        try:
            files = [stack.enter_context(open(fname)) for fname in filenames]
        except FileNotFoundError:
            print(f'Could not open all files: {filenames}')
        else:
            count, lines = check_files(*files)
            if count != None:
                if count >= 0:
                    print(f'Difference found at line {count}')
                    for file_handle, line in zip(files, lines):
                        print(f'{file_handle.name} contained:\n{line.rstrip()}')
                elif count < 0:
                    print(
                        f'Different file lenghts found after line {-count-1}')
                    for file_handle, line in zip(files, lines):
                        if line:
                            print(
                                f'{file_handle.name} contained:\n{line.rstrip()}')
                        else:
                            print(f'{file_handle.name} ended')
            else:
                print('No differences found')
