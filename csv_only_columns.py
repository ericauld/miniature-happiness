#!/usr/bin/env python3
import csv
import os
import sys
import re

try:
    sys.stdin.reconfigure(newline='')
    sys.stdout.reconfigure(newline='')
    y = csv.DictReader(sys.stdin)

    pattern = "|".join(sys.argv[1:])    
    fieldnames = [name for name in y.fieldnames if re.search(pattern, name, re.IGNORECASE)]
    z = csv.DictWriter(sys.stdout, fieldnames)

    z.writeheader()
    for row in y:
        z.writerow({key: row[key] for key in fieldnames})
    sys.stdout.flush()
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)
