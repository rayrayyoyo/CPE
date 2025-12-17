# -*- coding: utf-8 -*-
import sys

# 公式：點 (x, y) 在第 n = x + y 條對角線上
# 該點之前的點數總和 = (0+1+...+n) + x
def get_pos(x, y):
    n = x + y
    # 1 + 2 + ... + n = n*(n+1)/2
    # 加上該層的 x 偏移量
    return (n * (n + 1)) // 2 + x

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    n_cases = int(next(iterator))
    for i in range(1, n_cases + 1):
        x1 = int(next(iterator))
        y1 = int(next(iterator))
        x2 = int(next(iterator))
        y2 = int(next(iterator))
        
        diff = get_pos(x2, y2) - get_pos(x1, y1)
        print(f"Case {i}: {diff}")
except StopIteration:
    pass