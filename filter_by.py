#!/usr/bin/env python3
import csv
import sys
import re
import os

sys.stdin.reconfigure(newline='')
sys.stdout.reconfigure(newline='')
y = csv.DictReader(sys.stdin)
z = csv.DictWriter(sys.stdout, y.fieldnames)
matching_fields = [x for x in y.fieldnames if re.search(sys.argv[1], x, re.IGNORECASE)]
assert(len(matching_fields)==1)
filtered_field = matching_fields[0]
try:
    z.writeheader()
    for row in y:
        for s in sys.argv[2:]:
            if re.search(s, row[filtered_field], re.IGNORECASE):
                z.writerow(row)
                break
    sys.stdout.flush()
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)

