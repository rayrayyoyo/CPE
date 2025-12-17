# -*- coding: utf-8 -*-
import sys

case_num = 1
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    while True:
        n = int(next(iterator))
        m = int(next(iterator))
        
        if n == 0 and m == 0:
            break
            
        if case_num > 1:
            print()
            
        # 讀取地圖
        grid = []
        for _ in range(n):
            grid.append(list(next(iterator)))
            
        print(f"Field #{case_num}:")
        
        # 建立答案矩陣
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '*':
                    print('*', end='')
                else:
                    count = 0
                    # 檢查九宮格
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                                count += 1
                    print(count, end='')
            print() # 換行
            
        case_num += 1
except StopIteration:
    pass