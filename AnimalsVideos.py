def main():
    
    import csv
    
    my_file = open('animalVideos.csv', 'r')

    list_of_lines = csv.reader(my_file, delimiter=',')
    next(list_of_lines, None) # skip header row
    
    counter = 0
    sum = 0
    longest = 0
    shortest = 9999
    longname = ''
    shortname = ''

    for line_items in list_of_lines:
        colon = line_items[2].find(":")
        if colon < 0:
            seconds = int(line_items[2])*60
        elif colon == 0:
            seconds = int(line_items[2][1:])
        else:
            seconds = int(line_items[2][:colon])*60 + int(line_items[2][colon+1:])
        print(f'Name: {line_items[0]}, length: {seconds} seconds.')

        sum += seconds
        counter += 1
        if seconds < shortest:
            shortest = seconds
            shortname = line_items[0]
        if seconds > longest:
            longest = seconds
            longname = line_items[0]
    
    average = round(sum / counter)
    sum = round(sum)
    print(f'Sum:    \t{sum//60:4d}:{sum%60} ({sum} seconds).')
    print(f'Average:\t{average//60:4d}:{average%60} ({average} seconds).')
    print(f'Longest:\t{longname} at {longest//60}:{longest%60} ({longest} seconds).')
    print(f'Shortest:\t{shortname} at {shortest//60}:{shortest%60} ({shortest} seconds).')

if __name__ == "__main__":
    main()