#!/usr/bin/env python3
import csv
import sys
import re
import os
import random

class ReservoirSampler:
    def __init__(self, k):
        self.k = k
        self.count = 0
        self.reservoir = [None for i in range(k)]

    def sample(self, x):
        if (self.count < self.k):
            self.reservoir[self.count] = x
            self.count += 1
        else:
            self.count += 1
            # w prob k / count, swap w a random element from reservoir
            rn = random.randrange(self.count)
            if (rn < k):
                rn2 = random.randrange(k)
                self.reservoir[rn2] = x

    def __iter__(self):
        return iter(self.reservoir)

y = csv.DictReader(sys.stdin)
print(','.join(y.fieldnames))
k = int(sys.argv[1])
rs = ReservoirSampler(k)
try :
    for row in y:
        if row['Language'] == 'en':
            for s in sys.argv[2:]:
                if re.search(s, row['Subjects'], re.IGNORECASE):
                    rs.sample(row)
    for row in rs:
        print(','.join(v for _, v in row.items()))
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)

