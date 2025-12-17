# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 2:
            continue
            
        a = int(parts[0])
        b = int(parts[1])
        
        print(abs(b - a))
    except ValueError:
        break