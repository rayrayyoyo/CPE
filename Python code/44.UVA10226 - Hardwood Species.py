# -*- coding: utf-8 -*-
import sys
from collections import Counter

# 一次讀取所有輸入，避免 I/O 延遲
input_data = sys.stdin.read().splitlines()
iterator = iter(input_data)

try:
    # 第一行是測資數量
    first_line = next(iterator)
    if not first_line:
        # 處理可能的空行
        first_line = next(iterator)
    T = int(first_line)
    
    # 跳過第一筆測資前的空行
    next(iterator)
    
    for t in range(T):
        if t > 0:
            print() # 每個 Case 之間要有空行
            
        trees = []
        while True:
            try:
                line = next(iterator)
                if not line: # 遇到空行代表該 Case 結束
                    break
                trees.append(line)
            except StopIteration:
                break
        
        # 使用 Counter 加速統計 O(N)
        counts = Counter(trees)
        total = len(trees)
        
        # 題目要求按字母排序輸出
        sorted_names = sorted(counts.keys())
        
        for name in sorted_names:
            percentage = (counts[name] / total) * 100
            print(f"{name} {percentage:.4f}")
            
except StopIteration:
    pass