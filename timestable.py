def times_tables(tables=12, factors=12):
    ''' print the times tables.

    Params:
        tables, default 12, number of tables starting at 1
        factors, default 12, highest factor to multiple by in each table

    Returns:
        string: formatted output of times tables
    '''
    output = f'\nThe {tables} times tables\n'
    for table in range(1, tables + 1):
        output += f'\n\n{table:2d} times table\n{"_" * 14}\n'
        for factor in range(1, factors + 1):
            output += f'{table:2d} x {factor:2d} = {table * factor :3d}\n'
    return output

if __name__ == "__main__":
    print(times_tables(4))
    print(times_tables(5, 3))