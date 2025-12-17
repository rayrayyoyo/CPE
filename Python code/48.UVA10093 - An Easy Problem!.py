# -*- coding: utf-8 -*-
import sys

# 建立字元對照表
values = {}
# 0-9
for i in range(10):
    values[str(i)] = i
# A-Z (10-35)
for i in range(26):
    values[chr(ord('A') + i)] = i + 10
# a-z (36-61)
for i in range(26):
    values[chr(ord('a') + i)] = i + 36

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        
        # 處理正負號，其實不影響總和的整除性
        raw_line = line
        if line.startswith('-') or line.startswith('+'):
            line = line[1:]
            
        max_val = 1 # 最小進位制至少是 2 (所以 max_val 初始至少為 1)
        total_sum = 0
        
        for char in line:
            if char in values:
                val = values[char]
                max_val = max(max_val, val)
                total_sum += val
                
        # 從 max_val + 1 開始嘗試，直到 62 進位
        found = False
        for base in range(max_val + 1, 63):
            # 題目原理：若 N 在 Base 進位下能被 Base-1 整除，
            # 則各位數之和 sum 也能被 Base-1 整除。
            if total_sum % (base - 1) == 0:
                print(base)
                found = True
                break
        
        if not found:
            print("such number is impossible!")

solve()