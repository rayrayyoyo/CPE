# -*- coding: utf-8 -*-
import sys

# 讀取 float 比較保險的方式
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    while True:
        coords = []
        # 一次讀 8 個數字
        for _ in range(8):
            coords.append(float(next(iterator)))
            
        x1, y1 = coords[0], coords[1]
        x2, y2 = coords[2], coords[3]
        x3, y3 = coords[4], coords[5]
        x4, y4 = coords[6], coords[7]
        
        # 找出重複的點
        # 向量公式：D = A + C - B (其中 B 是重複點)
        rx, ry = 0, 0
        
        if x1 == x3 and y1 == y3:
            rx = x2 + x4 - x1
            ry = y2 + y4 - y1
        elif x1 == x4 and y1 == y4:
            rx = x2 + x3 - x1
            ry = y2 + y3 - y1
        elif x2 == x3 and y2 == y3:
            rx = x1 + x4 - x2
            ry = y1 + y4 - y2
        elif x2 == x4 and y2 == y4:
            rx = x1 + x3 - x2
            ry = y1 + y3 - y2
            
        print(f"{rx:.3f} {ry:.3f}")
        
except StopIteration:
    pass