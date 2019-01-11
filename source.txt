# generate 10 random numbers and print lowest
import random
loops = 10
maxtries = 100000
topnumber = maxtries
msg = "not set yet"  # this should never be used as break or else on for sets
for _ in range(loops):  # do this n times
    lowest = topnumber  # set to top of  range being generated for each  do over
    for i in range(maxtries):  # loop 0 to n-1
        r = random.randint(0, topnumber)
        if r < lowest:
            lowest = r
            if lowest == 0:
                msg = "on go {}.".format(i)
                break
    else:
        msg = "Not low enough!"
    print("Lowest was: {} {}".format(lowest, msg))
