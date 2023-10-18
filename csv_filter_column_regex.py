#!/usr/bin/env python3

import csv
import sys
import os
import re

try:
    sys.stdin.reconfigure(newline='')
    sys.stdout.reconfigure(newline='')

    y = csv.DictReader(sys.stdin)
    z = csv.DictWriter(sys.stdout, y.fieldnames)

    column_name = sys.argv[1]
    pattern = sys.argv[2]

    z.writeheader()
    for row in y:
        column_value = row[column_name]
        if re.search(pattern, column_value, re.IGNORECASE):
            z.writerow(row)
    sys.stdout.flush()
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)
