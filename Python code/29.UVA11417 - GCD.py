# -*- coding: utf-8 -*-
import sys
import math

# 由於 N <= 500，直接跑雙層迴圈不會超時
for line in sys.stdin:
    try:
        N = int(line)
    except ValueError:
        continue
        
    if N == 0:
        break
        
    G = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            G += math.gcd(i, j)
            
    print(G)