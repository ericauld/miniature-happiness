#!/usr/bin/env python3

import csv
import sys
import random
import os


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

try:
    sys.stdin.reconfigure(newline='')
    sys.stdout.reconfigure(newline='')

    y = csv.reader(sys.stdin)
    z = csv.writer(sys.stdout)

    k = int(sys.argv[1])
    rs = ReservoirSampler(k)

    header = next(y)
    for row in y:
        rs.sample(row)
    z.writerow(header)
    for row in rs:
        if row is not None:
            z.writerow(row)
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)

