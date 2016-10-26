#! /usr/bin/env python3

import difflib, sys

if len(sys.argv) != 3:
    sys.stderr.write("Useage: simplediff.py <old> <new>\n")
    sys.exit(1)

with open(sys.argv[1]) as fromf, open(sys.argv[2]) as tof:
    for line in difflib.unified_diff(list(fromf), list(tof), 
                                     fromfile=sys.argv[1], tofile=sys.argv[2]):
        sys.stdout.write(line) 

