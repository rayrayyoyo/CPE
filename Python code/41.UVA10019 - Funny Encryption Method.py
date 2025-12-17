# -*- coding: utf-8 -*-
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    N = int(next(iterator))
    for _ in range(N):
        M_str = next(iterator)
        M_val = int(M_str)
        
        # 1. 十進位的 Hex 轉 Binary 有幾個 1
        b1 = bin(M_val).count('1')
        
        # 2. 十六進位 (直接把輸入字串當 Hex 看) 轉 Binary 有幾個 1
        # 例如輸入 "265"，當作 Hex 0x265 處理
        hex_val = int(M_str, 16)
        b2 = bin(hex_val).count('1')
        
        print(f"{b1} {b2}")
except StopIteration:
    pass