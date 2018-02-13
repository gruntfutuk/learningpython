''' problem on /r/learnpython

    How can I write part of dictionary value string as headers to csv file in python? Is there a better way?
    by aqualh

    I have a dictionary that uses log file names as keys. When reading through a text file if it contains a value I was searching for, it saves the entire line as a new value in the list of values for that key(log file name).
    I.e Key: logFile0 Value: [Val1 5, Val2 3, Val3 72]. I want to output to a csv file the values as headers and which log file it was found and the value.
    I want it to be displayed in the csv file where for each time the value was found in the log file, it's value is displayed as:
    https://pastebin.com/U5ECptWL
'''

def dummy():
    '''generate dummy data'''
    VALUENAMES = [f'val{x:03d}' for x in range(20)]
    from random import randint
    dummyd = dict()
    for lognum in range(1, 50):
        log = 'log'+str(lognum)
        dummyd[log] = []
        valnames = list(VALUENAMES)
        for _ in range(randint(4, 10)):
            dummyd[log].append(f'{valnames.pop(randint(0, len(valnames) - 1))} {randint(1, 50)}')
    return dummyd

def headers(dumdata):
    '''generate csv headers'''

    rowset = set()
    for vals in dumdata.values():
        for val in vals:
            valname, valnum = val.split()
            rowset.add(valname)

    return list(sorted(rowset))

def rows(dumdata, valuenames, writer):
    '''generate rows for csv file'''

    for log, vals in dumdata.items():
        rowvals = [log]
        valdict = dict(val.split() for val in vals)
        for valname in valuenames:
            valnum = valdict.get(valname)
            if valnum:
                rowvals.append(valnum)
            else:
                rowvals.append(None)
        writer.writerow(rowvals)


import csv
with open('output.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # dumdata = dummy()
    dumdata = {'log1': ['val001 36', 'val005 46', 'val006 22', 'val002 1', 'val012 37'], 'log2': ['val000 38', 'val016 8', 'val018 46', 'val006 48', 'val010 3', 'val019 31', 'val012 13', 'val001 24', 'val002 43', 'val005 10'], 'log3': ['val015 40', 'val012 12', 'val013 22', 'val017 11', 'val016 12', 'val008 21', 'val010 18', 'val000 42', 'val014 11'], 'log4': ['val003 6', 'val000 36', 'val002 30', 'val019 42', 'val009 2', 'val013 9', 'val012 13', 'val007 49'], 'log5': ['val013 25', 'val004 50', 'val008 12', 'val019 30', 'val016 10', 'val000 44', 'val006 40', 'val015 48', 'val014 4', 'val007 17'], 'log6': ['val000 35', 'val002 15', 'val010 22', 'val014 42', 'val015 21', 'val005 9', 'val013 1', 'val011 33', 'val007 11', 'val012 9'], 'log7': ['val013 11', 'val000 2', 'val017 7', 'val004 6', 'val014 24', 'val011 49', 'val016 25'], 'log8': ['val009 13', 'val004 34', 'val013 7', 'val015 18', 'val005 16', 'val018 14'], 'log9': ['val004 11', 'val007 42', 'val005 28', 'val001 32', 'val011 13', 'val008 7', 'val010 46', 'val006 13'], 'log10': ['val009 38', 'val008 45', 'val011 1', 'val001 6'], 'log11': ['val009 48', 'val018 27', 'val007 19', 'val001 25', 'val016 43', 'val014 39', 'val008 25', 'val012 43', 'val004 4', 'val003 48'], 'log12': ['val003 46', 'val004 22', 'val014 12', 'val015 5', 'val019 16', 'val001 30', 'val010 18', 'val017 37', 'val013 22'], 'log13': ['val012 34', 'val002 43', 'val003 43', 'val017 42', 'val015 11', 'val016 16'], 'log14': ['val003 24', 'val013 34', 'val001 20', 'val011 36', 'val008 21', 'val000 46'], 'log15': ['val016 24', 'val008 15', 'val003 5', 'val017 50'], 'log16': ['val009 38', 'val000 41', 'val003 21', 'val005 6', 'val010 45', 'val013 32', 'val012 9', 'val008 35'], 'log17': ['val010 17', 'val017 9', 'val014 30', 'val005 20', 'val001 32'], 'log18': ['val007 43', 'val014 21', 'val017 43', 'val012 5', 'val001 48'], 'log19': ['val013 11', 'val010 14', 'val019 3', 'val002 44'], 'log20': ['val007 3', 'val006 3', 'val014 27', 'val001 4'], 'log21': ['val009 28', 'val004 12', 'val019 31', 'val011 11', 'val005 25', 'val012 48'], 'log22': ['val015 13', 'val009 6', 'val000 3', 'val002 16', 'val005 3', 'val010 35', 'val018 27', 'val016 21', 'val004 4'], 'log23': ['val012 33', 'val001 27', 'val018 24', 'val019 16', 'val008 50', 'val015 25', 'val007 27', 'val010 39'], 'log24': ['val018 1', 'val017 32', 'val016 6', 'val003 37'], 'log25': ['val017 19', 'val002 8', 'val014 39', 'val012 7', 'val015 8'], 'log26': ['val013 17', 'val012 14', 'val006 21', 'val018 40', 'val015 32', 'val019 41', 'val007 19', 'val003 29'], 'log27': ['val017 29', 'val005 1', 'val006 16', 'val019 38', 'val013 20', 'val008 46', 'val012 23', 'val016 30', 'val011 41', 'val000 5'], 'log28': ['val019 29', 'val015 23', 'val003 9', 'val010 18', 'val012 23', 'val011 31', 'val014 11', 'val009 46'], 'log29': ['val009 28', 'val000 38', 'val008 22', 'val017 6'], 'log30': ['val018 35', 'val013 10', 'val005 39', 'val003 38', 'val002 22', 'val011 10', 'val016 23', 'val014 17', 'val009 9', 'val019 48'], 'log31': ['val010 35', 'val012 18', 'val018 28', 'val002 36', 'val011 49', 'val000 33'], 'log32': ['val003 41', 'val014 15', 'val000 34', 'val015 7'], 'log33': ['val003 4', 'val012 30', 'val001 43', 'val009 34', 'val013 6'], 'log34': ['val017 47', 'val013 17', 'val008 15', 'val006 34', 'val002 17', 'val004 43'], 'log35': ['val011 17', 'val018 43', 'val005 35', 'val008 19', 'val013 46', 'val010 33', 'val014 41', 'val000 15', 'val009 16'], 'log36': ['val014 4', 'val017 5', 'val010 31', 'val001 9', 'val000 19', 'val005 43'], 'log37': ['val003 4', 'val019 39', 'val005 14', 'val001 15', 'val014 21', 'val002 6', 'val009 24', 'val011 33', 'val010 35', 'val006 29'], 'log38': ['val017 19', 'val007 4', 'val016 34', 'val014 8', 'val000 11', 'val004 28', 'val009 10'], 'log39': ['val013 40', 'val001 26', 'val003 25', 'val017 47', 'val011 1', 'val018 30', 'val000 41', 'val004 26', 'val016 15'], 'log40': ['val005 35', 'val013 48', 'val010 32', 'val019 1', 'val002 29', 'val011 14', 'val007 16'], 'log41': ['val009 13', 'val014 11', 'val003 45', 'val010 7'], 'log42': ['val013 25', 'val012 4', 'val014 10', 'val003 50', 'val001 28', 'val016 46', 'val015 20', 'val006 38', 'val009 7'], 'log43': ['val011 44', 'val010 35', 'val014 15', 'val006 10', 'val013 2'], 'log44': ['val017 31', 'val015 23', 'val001 28', 'val018 5', 'val008 27', 'val019 41'], 'log45': ['val002 4', 'val018 20', 'val011 24', 'val005 18', 'val007 7', 'val009 21', 'val004 18', 'val001 16', 'val006 23', 'val015 35'], 'log46': ['val008 37', 'val000 3', 'val006 25', 'val017 43', 'val013 22', 'val011 46', 'val005 39', 'val010 41', 'val004 26', 'val015 48'], 'log47': ['val012 13', 'val002 45', 'val007 44', 'val015 40', 'val011 39', 'val010 19'], 'log48': ['val019 26', 'val017 27', 'val004 30', 'val003 44', 'val005 16', 'val007 46'], 'log49': ['val004 5', 'val008 50', 'val002 43', 'val009 23', 'val012 7', 'val013 19', 'val007 34', 'val010 7']}
    valuenames = headers(dumdata)
    writer.writerow(["log name"] + valuenames)
    rows(dumdata, valuenames, writer)

