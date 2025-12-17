# -*- coding: utf-8 -*-
import sys
import math

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
            
        a, b = map(int, line.split())
        
        if a == 0 and b == 0:
            break
            
        # 優化解法：
        # 計算 1~b 之間有幾個完全平方數 -> floor(sqrt(b))
        # 計算 1~(a-1) 之間有幾個完全平方數 -> floor(sqrt(a-1))
        # 兩者相減就是 [a, b] 之間的數量
        
        sqrt_b = int(math.floor(b ** 0.5))
        sqrt_a_minus_1 = int(math.floor((a - 1) ** 0.5))
        
        print(sqrt_b - sqrt_a_minus_1)
        
    except ValueError:
        break