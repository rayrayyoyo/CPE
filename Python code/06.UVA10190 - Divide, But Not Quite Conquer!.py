# -*- coding: utf-8 -*-
import sys

# 讀取所有輸入直到 EOF
for line in sys.stdin:
    # 去除前後空白，如果這行是空的就跳過
    if not line.strip():
        continue
        
    try:
        n, m = map(int, line.split())
    except ValueError:
        continue

    # 題目條件：n 和 m 都要大於 1，否則無法進行除法序列
    if n < 2 or m < 2:
        print("Boring!")
        continue

    ans = [n]
    
    # 開始除法邏輯
    while n > 1:
        if n % m == 0:
            n //= m
            ans.append(n)
        else:
            # 不能整除，直接跳出
            break
            
    # 如果最後除到剩 1，代表成功
    if ans[-1] == 1:
        print(" ".join(map(str, ans)))
    else:
        print("Boring!")