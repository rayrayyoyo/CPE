# -*- coding: utf-8 -*-
import sys

first = True

for line in sys.stdin:
    # 讀取整行包含換行符號，但通常我們只計算可見字元
    # 題目要求 ASCII 32~128，但 Python strip() 會去掉換行
    line = line.strip('\n').strip('\r')
    
    if not line: # 處理空行情況
        continue

    if not first:
        print()
    first = False

    counts = {}
    for char in line:
        val = ord(char)
        counts[val] = counts.get(val, 0) + 1
    
    # 排序規則：頻率(x[1]) 由小到大，若相同則 ASCII(x[0]) 由大到小(-x[0])
    sorted_items = sorted(counts.items(), key=lambda x: (x[1], -x[0]))
    
    for k, v in sorted_items:
        print(f"{k} {v}")