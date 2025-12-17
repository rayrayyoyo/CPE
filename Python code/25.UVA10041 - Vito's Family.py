# -*- coding: utf-8 -*-
import sys

# 讀取所有輸入
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    cases = int(next(iterator))
    for _ in range(cases):
        r = int(next(iterator)) # 親戚數量
        street_nums = []
        for _ in range(r):
            street_nums.append(int(next(iterator)))
            
        street_nums.sort()
        
        # 找中位數
        mid = street_nums[r // 2]
        
        dist = sum(abs(x - mid) for x in street_nums)
        print(dist)
except StopIteration:
    pass