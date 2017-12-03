from sys import argv
from os.path import exists

script, source, dest = argv


copy = open(source).read()
open(dest,"w").write(copy)
