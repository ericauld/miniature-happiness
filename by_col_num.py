#!/usr/bin/env python3
import csv
import os
import sys

x = csv.reader(sys.stdin)
try:
    for row in x:
        for s in sys.argv[1:]:
            print(row[int(s)], end=" ")
        print()
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)
