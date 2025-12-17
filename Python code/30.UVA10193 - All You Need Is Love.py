# -*- coding: utf-8 -*-
import sys
import math

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    N = int(next(iterator))
    for i in range(1, N + 1):
        s1 = next(iterator)
        s2 = next(iterator)
        
        # 將二進位字串轉為整數
        n1 = int(s1, 2)
        n2 = int(s2, 2)
        
        if math.gcd(n1, n2) > 1:
            print(f"Pair #{i}: All you need is love!")
        else:
            print(f"Pair #{i}: Love is not all you need!")
except StopIteration:
    pass