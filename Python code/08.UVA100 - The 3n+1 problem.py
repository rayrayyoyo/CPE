# -*- coding: utf-8 -*-
import sys

def f(n):
    if n % 2 != 0:
        return n * 3 + 1
    else:
        return n // 2

# 使用 sys.stdin 讀取效率較高，也自動處理 EOF
for line in sys.stdin:
    if not line.strip():
        continue
        
    i, j = map(int, line.split())

    # 題目要求輸出原本的順序，但計算要從小的到大的
    min1 = min(i, j)
    max1 = max(i, j)
    
    max_cycle = 0

    for k in range(min1, max1 + 1):
        l = 1
        curr = k
        while curr != 1:
            curr = f(curr)
            l += 1
        
        if l > max_cycle:
            max_cycle = l

    print(i, j, max_cycle)