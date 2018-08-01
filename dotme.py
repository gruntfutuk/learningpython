#!/usr/bin/env python

import re
import argparse
import sys


parser = argparse.ArgumentParser('Format Python scripts for FaceBook readability')
parser.add_argument('--infile', type=argparse.FileType(), help='Name of file to convert',
                    default=sys.stdin)
parser.add_argument('--outfile', type=argparse.FileType('w'), help='Converted file name',
                    default=sys.stdout)
opts = parser.parse_args()

def convert_func(matchobj):
    prefix = matchobj.group(0)
    replace_symbol = set(' .').difference(prefix[0]).pop()
    return replace_symbol * len(prefix)

for line in opts.infile:
    if line.strip() and line[0] in ' .':
        line = re.sub(r'^(.)\1*', convert_func, line)
    opts.outfile.write(line)
