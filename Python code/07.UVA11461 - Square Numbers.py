# -*- coding: utf-8 -*-
import sys
import math

while True:
    try:
        line = sys.stdin.readline()
            
        a, b = map(int, line.split())
        
        if a == 0 and b == 0:
            break
        
        sqrt_b = int(math.floor(b ** 0.5))
        sqrt_a_minus_1 = int(math.floor((a - 1) ** 0.5))
        
        print(sqrt_b - sqrt_a_minus_1)
        
    except ValueError:
        break