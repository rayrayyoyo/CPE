# -*- coding: utf-8 -*-
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    while True:
        n = int(next(iterator))
        nums = []
        for _ in range(n):
            nums.append(int(next(iterator)))
            
        nums.sort()
        
        mid1 = nums[(n - 1) // 2]
        mid2 = nums[n // 2]
        
        # 1. 最小的中位數
        min_median = mid1
        
        # 2. 數列中有多少數字等於其中一個中位數
        count = 0
        for x in nums:
            if x == mid1 or x == mid2:
                count += 1
                
        # 3. 可能的整數中位數共有幾個 (mid2 - mid1 + 1)
        possible_medians = mid2 - mid1 + 1
        
        print(f"{min_median} {count} {possible_medians}")
        
except StopIteration:
    pass