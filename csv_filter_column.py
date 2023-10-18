#!/usr/bin/env python3

import csv
import sys
import os

try:
    sys.stdin.reconfigure(newline='')
    sys.stdout.reconfigure(newline='')

    y = csv.DictReader(sys.stdin)
    z = csv.DictWriter(sys.stdout, y.fieldnames)

    column_name = sys.argv[1]
    column_value = sys.argv[2]
    
    z.writeheader()
    for row in y:
        if row[column_name] == column_value:
            z.writerow(row)
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)
