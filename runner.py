'example python code to run another python script, passed on command line'
'initially set up to be keeprunning.py and re-start it if it fails'
'for any reason other than returning exit code 101'
'example usage: python3 runner.py keeprunning.py'

from subprocess import Popen
import sys

filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
    if p.returncode == 101:
        break
