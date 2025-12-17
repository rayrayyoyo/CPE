# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 2: continue
        v = int(parts[0])
        t = int(parts[1])
        print(2 * v * t)
    except ValueError:
        break