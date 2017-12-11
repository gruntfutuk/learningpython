import xlwt
import os

#cygwin_path='C:\cygwin64\bin\'

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Totals",cell_overwrite_ok=True)


envs = ['<folder>', '<folder>', '<folder>', '<folder>',
        '<folder>', '<folder>']


row = 0
col = 0
col1 = 0
col2= 1
for env in envs:
    row1 = 1
    row2 = 1
    list2 = []
    list = []
    print env
    sheet.write(row, col, env)
    col += 3
    dates = os.popen('cmd /c "cd /d R:\'+env+'\<folder> && C:\cygwin64\bin\find_linux.exe . -type f -printf "%TY-%Tm-%Td\n" | sort | C:\cygwin64\bin\uniq -c | C:\cygwin64\bin\gawk "{print $2}""').read()
    count = os.popen('cmd /c "cd /d R:\'+env+'\<folder> && C:\cygwin64\bin\find_linux.exe . -type f -printf "%TY-%Tm-%Td\n" | sort | C:\cygwin64\bin\uniq -c | C:\cygwin64\bin\gawk "{print $1}""').read()
    if dates =='':
        list2.append('Empty')
    else:
        list2.append(dates)

    if count =='':
        list.append('Empty')
    else:
        list.append(count)

    for seperator2 in list2:
        date_list = seperator2.split()
        for x in date_list:
            sheet.write(row1, col1, x)
            row1 +=1
        col1 += 3

    for seperator in list:
        count_list = seperator.split()
        for y in count_list:
            sheet.write(row2, col2, y)
            row2 +=1
        col2 += 3

workbook.save("D:\TOTALS.xls")