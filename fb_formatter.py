#!/usr/bin/env python

import re
import argparse


parser = argparse.ArgumentParser('Format Python scripts for FaceBook readability')
parser.add_argument('in_file', type=argparse.FileType(), help='Name of file to convert')
parser.add_argument('out_file',type=argparse.FileType('w'), help='Converted file name')
opts = parser.parse_args()

def convert_func(matchobj):
    prefix = matchobj.group(0)
    replace_symbol = set(' .').difference(prefix[0]).pop()
    return replace_symbol * len(prefix)

for line in opts.in_file:
    if line.strip() and line[0] in ' .':
        line = re.sub(r'^(.)\1*', convert_func, line)
    opts.out_file.write(line)
                                                    
