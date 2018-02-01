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
    dumdata = dummy()
    valuenames = headers(dumdata)
    writer.writerow(["log name"] + [valuenames])
    rows(dumdata, valuenames, writer)

