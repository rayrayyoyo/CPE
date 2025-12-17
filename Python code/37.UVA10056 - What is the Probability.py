# -*- coding: utf-8 -*-
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    S = int(next(iterator))
    for _ in range(S):
        N = int(next(iterator))
        p = float(next(iterator))
        i = int(next(iterator))
        
        if p == 0:
            print("0.0000")
        else:
            q = 1 - p
            # 公式：首項 a = p * q^(i-1)
            # 公比 r = q^N
            # 無窮等比級數和 S = a / (1 - r)
            r = q ** N
            a = p * (q ** (i - 1))
            ans = a / (1 - r)
            print(f"{ans:.4f}")
except StopIteration:
    pass