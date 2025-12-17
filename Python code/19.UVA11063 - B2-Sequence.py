# -*- coding: utf-8 -*-
import sys

case_num = 1
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    while True:
        # 讀取 N
        N = int(next(iterator))
        
        # 讀取接下來 N 個數字
        nums = []
        for _ in range(N):
            nums.append(int(next(iterator)))
            
        # 檢查條件 1: 嚴格遞增且大於等於 1
        is_b2 = True
        if nums[0] < 1:
            is_b2 = False
        
        for k in range(N - 1):
            if nums[k] >= nums[k+1]:
                is_b2 = False
                break
        
        if is_b2:
            # 檢查條件 2: 兩數之和不重複
            sums = set()
            for i in range(N):
                for j in range(i, N): # j 從 i 開始 (包含自己加自己)
                    s = nums[i] + nums[j]
                    if s in sums:
                        is_b2 = False
                        break
                    sums.add(s)
                if not is_b2:
                    break
        
        if is_b2:
            print(f"Case #{case_num}: It is a B2-Sequence.")
        else:
            print(f"Case #{case_num}: It is not a B2-Sequence.")
            
        print() # 每個 Case 後面要空一行
        case_num += 1
        
except StopIteration:
    pass