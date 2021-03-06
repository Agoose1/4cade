#!/usr/bin/env python3

import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWX'
coords = []
for filename in ('crystal1.txt','crystal2.txt','crystal3.txt','crystal4.txt'):
    with open(filename) as f:
        lines = f.readlines()
    for c in alphabet:
        for line, row in zip(lines, range(len(lines))):
            for l, col in zip(line, range(len(line))):
                if l == c:
                    if (row, col) not in coords:
                        coords.append((row, col))
        coords.append((255,255))
for row, col in coords:
    print("         !byte %s,%s" % (row, col))
