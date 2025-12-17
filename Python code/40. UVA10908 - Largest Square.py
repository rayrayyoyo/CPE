# -*- coding: utf-8 -*-
import sys

def check(arr, r, c, size, M, N):
    # 檢查邊界
    if r - size < 0 or r + size >= M or c - size < 0 or c + size >= N:
        return False
    
    char = arr[r][c]
    # 檢查正方形的「外框」是否都跟中心字元一樣
    # 上下邊
    for j in range(c - size, c + size + 1):
        if arr[r - size][j] != char or arr[r + size][j] != char:
            return False
    # 左右邊
    for i in range(r - size, r + size + 1):
        if arr[i][c - size] != char or arr[i][c + size] != char:
            return False
    return True

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)
    
    try:
        T_cases = int(next(iterator))
        for _ in range(T_cases):
            M = int(next(iterator))
            N = int(next(iterator))
            Q = int(next(iterator))
            
            print(f"{M} {N} {Q}") # 題目要求先輸出這行
            
            grid = []
            for _ in range(M):
                # 這裡要小心，split() 會把字串切開，但題目給的是連續字元
                # 如果用 iterator 讀取，每一行字串就是一個 row
                grid.append(next(iterator))
                
            for _ in range(Q):
                r = int(next(iterator))
                c = int(next(iterator))
                
                size = 1
                # size 代表「半徑」，邊長 = 2*size + 1
                # 嘗試擴展 size
                while check(grid, r, c, size, M, N):
                    size += 1
                
                # check 失敗時 size 已經多加了 1，所以要用 size-1 計算
                # 實際邊長 = 2 * (size-1) + 1
                print(2 * (size - 1) + 1)
                
    except StopIteration:
        pass

solve()