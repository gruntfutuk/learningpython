import time
x=0
for x in range(0,20):
    print(" ",time.ctime(), end="\r", flush=True)
    time.sleep(1)
