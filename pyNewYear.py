#!/usr/bin/env python
import os
import datetime
import time
import sys
import platform
from dateutil.relativedelta import relativedelta
from threading import Thread
try:
    import requests
except ImportError:
    os.system("pip install requests")


def download_file(url, local_fname):
    try:
        r = requests.get(url, stream=True)
        with open(local_fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)

        size = os.stat(local_fname).st_size / 1024
        if size > 1100:
            return True
        else:
            return False
    except:
        return False

def play_video(vid_name):
    os_name = platform.system()
    if "Linux" in os_name:
        os.system("xdg-open %s" % vid_name)
    elif "Windows" in os_name:
        os.system(vid_name)
    elif "Darwin" in os_name:
        os.system("open %s" % vid_name)

def count_down(future):
    diff = relativedelta(datetime.datetime.now(), future)
    days = abs(diff.days)
    hours = abs(diff.hours)
    mins = abs(diff.minutes)
    secs = abs(diff.seconds)
    return "\r%d days, %d hours, %d mins %d secs left.." % (days, hours, mins, secs)
    
def main():
    url = r"https://dl.dropboxusercontent.com/s/nq4p7klj6myaqea/python_2018.mp4?dl=0"
    target = datetime.datetime(2018, 1, 1, 00, 00, 00)
    downloaded = False
    while True:
        try:
            df = target - datetime.datetime.now()
            
            sys.stdout.write(count_down(target))
            time.sleep(1)
            sys.stdout.flush()
            
            if df.total_seconds() <= 300 and not downloaded:
                th = Thread(target=download_file, args= (url, "python_2018.mp4", ))
                th.start()
                downloaded = True

            if df.total_seconds() <= 4 and downloaded:
                play_video("python_2018.mp4")
                break

        except KeyboardInterrupt:
            sys.stdout.write("\nCouldn't wait eh? ._.")
            break

main()
