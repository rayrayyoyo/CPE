# -*- coding: utf-8 -*-
import sys

# 先建好費氏數列表，直到大於 100,000,000
fib = [0, 1]
while fib[-1] < 100000000:
    fib.append(fib[-1] + fib[-2])

# 讀取輸入
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    N = int(next(iterator))
    for _ in range(N):
        dec = int(next(iterator))
        print(f"{dec} = ", end="")
        
        flag = False # 用來標記是否已經開始輸出
        
        # 從最大的費氏數往下找 (index 2 開始是 1, 2, 3...)
        # 題目不使用 fib[0]=0, fib[1]=1，通常從 fib[2]=1 開始用
        for i in range(len(fib) - 1, 1, -1):
            if dec >= fib[i]:
                print("1", end="")
                dec -= fib[i]
                flag = True
            elif flag:
                print("0", end="")
                
        print(" (fib)")
except StopIteration:
    pass