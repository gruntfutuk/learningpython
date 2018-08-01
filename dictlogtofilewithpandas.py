import pandas as pd

def dummy():
    '''generate dummy data'''

    VALUENAMES = ['val{:03d}'.format(x) for x in range(1, 21)]
    from random import randint
    dummyd = dict()
    for lognum in range(1, 30):
        log = 'log' + str(lognum)
        dummyd[log] = []
        valnames = list(VALUENAMES)
            dummyd[log].append('{} {}'.format(vname, randint(1, 50)))
    return dummyd

def makedf(datadict):
    # empty df
    df = pd.DataFrame()

    # Iterate over each entry (log1-49)
    for entry in datadict:
        # create a series to hold the entry
        series = pd.Series(entry)

        for string in datadict[entry]:
            # split the value and column
            col, val = string.split(' ')
            # insert the value at the column, in the series
            series[col] = val

        # convert to dataframe to transpose
        new_df = series.to_frame().T
        # concat with existing dataframe
        df = pd.concat([df, new_df])

    return df

# Get dummy dictionary
datadict = dummy()

# create dataframe
df = makedf(datadict)

# sort columns
df.rename(columns = {0:' lognames'}, inplace = True)
df = df.reindex(sorted(df.columns), axis='columns')

# write to csv
df.to_csv('output.csv')