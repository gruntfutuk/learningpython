from sys import argv
from os.path import exists

script, source, dest = argv

if exists(dest):
    input("%r already exists, RETURN to overwrite, or CNTRL-C to escape" % (dest))
copy = open(source).read()
open(dest, "w").write(copy)
