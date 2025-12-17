# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    parts = list(map(int, line.split()))
    
    # 有時候會讀到空行，要過濾掉
    if not parts:
        continue
        
    n = parts[0]
    
    # 題目可能只有一個數字 n，後面沒數列 (雖然很少見)
    if n == 0: # 只有 0 個數字不算 Jolly (或看題目定義，通常 n>0)
        print("Not jolly")
        continue
    
    # 如果只有一個數字 (n=1)，它是 Jolly
    if n == 1:
        print("Jolly")
        continue

    sequence = parts[1:]
    diffs = set()
    
    for i in range(len(sequence) - 1):
        d = abs(sequence[i] - sequence[i+1])
        if 1 <= d < n:
            diffs.add(d)
    
    # 檢查是否包含了 1 到 n-1 的所有差值
    if len(diffs) == n - 1:
        print("Jolly")
    else:
        print("Not jolly")