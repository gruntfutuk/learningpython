def clean_perc(value):
    try:
        float(value)
        return float(value)
    except:
        if '%' in value:
            index = value.find('%')
            num = value[:index]
            return float(num)
        elif '-' in value:
            try:
                neg = value.find('-')
                index = value.find('%')
                num = value[neg:index]
                num = (float(num) *-1)
                return float(num)
            except:
                print(value)
        else:
            try:
                float(value)
                num = float(value) * 100
                return float(num)
            except:
                print(value)


mylist = ['1.03%', '0.25', '-2.01%', '-0.01%']
for df2 in mylist:
    print(clean_perc(df2))