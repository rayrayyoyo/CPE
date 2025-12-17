# -*- coding: utf-8 -*-
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    cases = int(next(iterator))
    for _ in range(cases):
        L = int(next(iterator))
        arr = []
        for _ in range(L):
            arr.append(int(next(iterator)))
            
        swaps = 0
        # Bubble Sort 模擬
        for i in range(L):
            for j in range(L - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
                    
        print(f"Optimal train swapping takes {swaps} swaps.")
except StopIteration:
    pass