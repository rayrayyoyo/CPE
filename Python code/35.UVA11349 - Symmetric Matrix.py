# -*- coding: utf-8 -*-
import sys

# 讀取全部資料以處理跨行輸入
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    T = int(next(iterator))
    for t in range(1, T + 1):
        # 處理 N = 100 的輸入格式
        while True:
            token = next(iterator)
            if token == 'N': continue
            if token == '=': continue
            n = int(token)
            break
        
        matrix_elements = []
        is_valid = True
        
        # 讀取矩陣並檢查負數
        for _ in range(n * n):
            val = int(next(iterator))
            if val < 0: 
                is_valid = False
            matrix_elements.append(val)
            
        if is_valid:
            # 檢查中心對稱 (點對稱)
            # 即檢查陣列是否為迴文：A[i] == A[len-1-i]
            length = len(matrix_elements)
            for k in range(length // 2 + 1):
                if matrix_elements[k] != matrix_elements[length - 1 - k]:
                    is_valid = False
                    break
        
        if is_valid:
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

except StopIteration:
    pass